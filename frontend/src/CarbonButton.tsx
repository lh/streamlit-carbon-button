import React, { useEffect } from "react"
import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"

interface State {
  numClicks: number
  isDarkMode: boolean
}

class CarbonButton extends StreamlitComponentBase<State> {
  public state = { numClicks: 0, isDarkMode: false }

  public componentDidMount() {
    console.log("CarbonButton mounted with props:", this.props)
    console.log("Args from Streamlit:", this.props.args)

    // CRITICAL: Set initial value from default prop
    const initialValue = this.props.args?.default || 0
    this.setState({ numClicks: initialValue }, () => {
      // Send initial value to Streamlit
      Streamlit.setComponentValue(this.state.numClicks)
      // IMPORTANT: Set frame height after component mounts
      Streamlit.setFrameHeight()
    })

    // Add global styles for SVG icons
    const style = document.createElement('style')
    style.textContent = `
      .carbon-button-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 20px;
        height: 20px;
        flex-shrink: 0;
      }
      .carbon-button-icon svg {
        width: 100%;
        height: 100%;
        fill: currentColor;
      }
      .carbon-button-content {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        width: 100%;
      }
      .carbon-button-icon-only {
        padding: 0.75rem !important;
      }
    `
    document.head.appendChild(style)

    // Check for dark mode
    const checkDarkMode = () => {
      const isDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
      this.setState({ isDarkMode: isDark })
    }

    // Initial check
    checkDarkMode()

    // Listen for changes
    if (window.matchMedia) {
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', checkDarkMode)
    }
  }

  public componentWillUnmount() {
    // Clean up listener
    if (window.matchMedia) {
      const checkDarkMode = () => {
        const isDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
        this.setState({ isDarkMode: isDark })
      }
      window.matchMedia('(prefers-color-scheme: dark)').removeEventListener('change', checkDarkMode)
    }
  }

  public componentDidUpdate() {
    // Update frame height whenever component updates
    Streamlit.setFrameHeight()
  }

  public render = (): React.ReactNode => {
    // Show loading state if no args yet
    if (!this.props.args) {
      return <div style={{ padding: "10px", border: "1px solid #ccc" }}>Loading Carbon Button...</div>
    }

    const { label, icon, buttonType, disabled, useContainerWidth, colors, isDefault, ariaLabel } = this.props.args

    // Debug: Log what we're receiving
    console.log("Carbon Button Debug:", {
      label,
      hasIcon: !!icon,
      iconLength: icon?.length,
      iconPreview: icon?.substring(0, 100),
      buttonType,
      allArgs: this.props.args
    })

    // Extra debug - check if icon contains SVG
    if (icon) {
      console.log("Icon contains <svg>:", icon.includes('<svg'))
      console.log("Icon contains viewBox:", icon.includes('viewBox'))
    }

    const hasIcon = icon && icon.trim() !== ''
    const hasLabel = label && label.trim() !== ''
    const isIconOnly = hasIcon && !hasLabel

    // Adjust padding for visual balance
    // When icon + text: more padding on right to balance the visual weight
    // When icon only: equal padding
    let padding = "0.75rem 1rem"
    if (isIconOnly) {
      padding = "0.75rem"
    } else if (hasIcon && hasLabel) {
      // Asymmetric padding: less on left (icon side), more on right
      padding = "0.75rem 1.25rem 0.75rem 0.875rem"
    }

    // Apply teal shadow for default buttons
    let boxShadow = buttonType === "secondary" ? "0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.05)" : "none"
    let transform = "translateY(0)"

    if (isDefault && !disabled) {
      boxShadow = "0 4px 12px rgba(80, 228, 224, 0.4)"
      transform = "translateY(-2px)"
    }

    const buttonStyle: React.CSSProperties = {
      backgroundColor: this.getBackgroundColor(buttonType),
      color: this.getTextColor(buttonType),
      border: buttonType === "ghost" ? `1px solid ${this.getBorderColor(buttonType)}` : buttonType === "secondary" ? `1px solid ${this.getBorderColor(buttonType)}` : "none",
      padding: padding,
      fontSize: "14px",
      fontWeight: 400,
      borderRadius: 0,
      cursor: disabled ? "not-allowed" : "pointer",
      display: "inline-flex",
      alignItems: "center",
      justifyContent: "center",
      width: useContainerWidth ? "100%" : "auto",
      transition: "all 70ms cubic-bezier(0.2, 0, 0.38, 0.9)",
      fontFamily: '"IBM Plex Sans", system-ui, -apple-system, sans-serif',
      lineHeight: 1,
      opacity: disabled ? 0.5 : 1,
      boxShadow: boxShadow,
      transform: transform,
      outline: "none",
    }

    // Generate aria-label
    const computedAriaLabel = ariaLabel || (isIconOnly ? label || "Icon button" : undefined)

    return (
      <button
        style={buttonStyle}
        className={isIconOnly ? "carbon-button-icon-only" : ""}
        onClick={this.onClicked}
        disabled={disabled}
        onMouseEnter={(e) => this.handleHover(e, true)}
        onMouseLeave={(e) => this.handleHover(e, false)}
        onMouseDown={this.handleMouseDown}
        onMouseUp={this.handleMouseUp}
        aria-label={computedAriaLabel}
      >
        <div className="carbon-button-content">
          {hasIcon && (
            <span
              className="carbon-button-icon"
              dangerouslySetInnerHTML={{ __html: icon }}
            />
          )}
          {hasLabel && <span>{label}</span>}
        </div>
      </button>
    )
  }

  private getBackgroundColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.rest_bg && type === "secondary") {
      return this.props.args.colors.rest_bg
    }

    // Different colors for light/dark mode - subtle palette
    const lightColors: { [key: string]: string } = {
      primary: "#e6e2e2",      // Changed primary to your subtle grey
      secondary: "#e6e2e2",    // Your custom light mode color
      danger: "#f4e3e3",       // Softer danger color
      ghost: "transparent",
    }

    const darkColors: { [key: string]: string } = {
      primary: "#ecdcdc",      // Your pink-grey for dark mode
      secondary: "#ecdcdc",    // Your custom dark mode color
      danger: "#f0d0d0",       // Lighter pink for danger in dark mode
      ghost: "transparent",
    }

    const colors = this.state.isDarkMode ? darkColors : lightColors
    return colors[type] || colors.primary
  }

  private getTextColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.rest_text && type === "secondary") {
      return this.props.args.colors.rest_text
    }

    // Different text colors for light/dark mode
    if (this.state.isDarkMode) {
      const darkModeColors: { [key: string]: string } = {
        primary: "#1a1a1a",      // Dark text on pink-grey
        secondary: "#1a1a1a",    // Dark text for contrast
        danger: "#4a1414",       // Dark red text
        ghost: "#262626",
      }
      return darkModeColors[type] || darkModeColors.primary
    }

    const colors: { [key: string]: string } = {
      primary: "#1a1a1a",      // Dark text on light grey
      secondary: "#1a1a1a",    // Almost black for maximum contrast
      danger: "#4a1414",       // Dark red text
      ghost: "#262626",
    }
    return colors[type] || colors.primary
  }

  private getBorderColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.rest_border && type === "secondary") {
      return this.props.args.colors.rest_border
    }

    const lightColors: { [key: string]: string } = {
      primary: "#cccccc",      // Subtle grey border
      secondary: "#cccccc",
      danger: "#e0c0c0",       // Soft pink border
      ghost: "#e0e0e0",        // Light grey for ghost
    }

    const darkColors: { [key: string]: string } = {
      primary: "#404040",      // Dark grey border
      secondary: "#404040",    // Your dark mode border
      danger: "#5a4040",       // Muted red border
      ghost: "#404040",        // Dark grey for ghost
    }

    const colors = this.state.isDarkMode ? darkColors : lightColors
    return colors[type] || colors.primary
  }

  private getHoverBackgroundColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.hover_bg && type === "secondary") {
      return this.props.args.colors.hover_bg
    }

    const lightColors: { [key: string]: string } = {
      primary: "#f5f5f5",      // Light grey hover
      secondary: "#f5f5f5",    // Light mode hover
      danger: "#faf0f0",       // Light pink hover
      ghost: "#fafafa",        // Very light grey
    }

    const darkColors: { [key: string]: string } = {
      primary: "#4a4a4a",      // Medium grey hover
      secondary: "#f6f4f4",    // Dark mode hover
      danger: "#5a4343",       // Muted red hover
      ghost: "#2a2a2a",        // Dark grey hover
    }

    const colors = this.state.isDarkMode ? darkColors : lightColors
    return colors[type] || colors.primary
  }

  private getHoverTextColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.hover_text && type === "secondary") {
      return this.props.args.colors.hover_text
    }

    return this.getTextColor(type)
  }

  private getHoverBorderColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.hover_border && type === "secondary") {
      return this.props.args.colors.hover_border
    }

    return this.getBorderColor(type)
  }

  private getActiveBackgroundColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.active_bg && type === "secondary") {
      return this.props.args.colors.active_bg
    }

    const lightColors: { [key: string]: string } = {
      primary: "#50e4e0",      // Teal accent for all buttons
      secondary: "#50e4e0",    // Light mode teal
      danger: "#e4807a",       // Soft coral for danger
      ghost: "#50e4e0",        // Teal for ghost too
    }

    const darkColors: { [key: string]: string } = {
      primary: "#67cccc",      // Darker teal for dark mode
      secondary: "#67cccc",    // Dark mode teal
      danger: "#cc6666",       // Muted red
      ghost: "#67cccc",        // Teal for ghost
    }

    const colors = this.state.isDarkMode ? darkColors : lightColors
    return colors[type] || colors.primary
  }

  private getActiveTextColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.active_text && type === "secondary") {
      return this.props.args.colors.active_text
    }

    // Dark mode uses black text on teal (as per your design)
    if (this.state.isDarkMode) {
      return "#000000"
    }

    // Light mode uses white text on teal
    return "#ffffff"
  }

  private getActiveBorderColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.active_border && type === "secondary") {
      return this.props.args.colors.active_border
    }

    return this.getBorderColor(type)
  }

  private handleHover = (e: React.MouseEvent<HTMLButtonElement>, isHover: boolean) => {
    const button = e.currentTarget
    const type = this.props.args.buttonType || "primary"
    const isDefault = this.props.args.isDefault

    if (isHover) {
      button.style.backgroundColor = this.getHoverBackgroundColor(type)
      button.style.color = this.getHoverTextColor(type)
      button.style.borderColor = this.getHoverBorderColor(type)

      if (isDefault) {
        // Enhanced hover for default buttons
        button.style.transform = "translateY(-3px)"
        button.style.boxShadow = "0 6px 16px rgba(80, 228, 224, 0.5)"
      } else {
        button.style.transform = "translateY(-1px)"
        button.style.boxShadow = "0 2px 6px rgba(0, 0, 0, 0.15)"
      }
    } else {
      button.style.backgroundColor = this.getBackgroundColor(type)
      button.style.color = this.getTextColor(type)
      button.style.borderColor = this.getBorderColor(type)

      if (isDefault) {
        // Return to default button state
        button.style.transform = "translateY(-2px)"
        button.style.boxShadow = "0 4px 12px rgba(80, 228, 224, 0.4)"
      } else {
        button.style.transform = "translateY(0)"
        button.style.boxShadow = type === "secondary" ? "0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.05)" : "none"
      }
    }
  }

  private handleMouseDown = (e: React.MouseEvent<HTMLButtonElement>) => {
    const button = e.currentTarget
    const type = this.props.args.buttonType || "primary"

    button.style.backgroundColor = this.getActiveBackgroundColor(type)
    button.style.color = this.getActiveTextColor(type)
    button.style.borderColor = this.getActiveBorderColor(type)
    button.style.transform = "translateY(0)"
    button.style.boxShadow = "inset 0 1px 2px rgba(0, 0, 0, 0.2)"
  }

  private handleMouseUp = (e: React.MouseEvent<HTMLButtonElement>) => {
    // Return to hover state since mouse is still over the button
    this.handleHover(e, true)
  }

  private onClicked = (): void => {
    this.setState(
      prevState => ({ numClicks: prevState.numClicks + 1 }),
      () => Streamlit.setComponentValue(this.state.numClicks)
    )
  }
}

export default withStreamlitConnection(CarbonButton)
