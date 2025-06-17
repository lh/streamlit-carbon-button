# Default Button Feature - Design Decision

## The Question
Should the "default button" visual indicator be:
1. A feature of our Carbon Button component?
2. A feature of Streamlit itself?

## Decision: Make it a Carbon Button Feature

### Reasons:
1. **We control it** - We can implement it immediately without waiting for Streamlit
2. **Component-specific styling** - Animations can match Carbon Design System aesthetics
3. **No dependencies** - Works with any Streamlit version
4. **Customizable** - Users can choose animation style or disable it
5. **Progressive enhancement** - Doesn't break existing buttons

### Implementation Plan:

1. **Add new props to CarbonButton component:**
   ```typescript
   interface CarbonButtonProps {
     // existing props...
     isDefault?: boolean
     defaultStyle?: 'pulse' | 'glow' | 'breathe' | 'elevated' | 'ring'
   }
   ```

2. **Add animations to component CSS:**
   - Built into the component, not external CSS
   - Respects prefers-reduced-motion
   - Only applies when `isDefault=True`

3. **Python API:**
   ```python
   carbon_button(
       "Submit",
       button_type="primary",
       is_default=True,
       default_style="pulse"  # optional, defaults to "pulse"
   )
   ```

### Benefits over Streamlit-level feature:
- Immediate availability
- Tailored to Carbon Design System
- No coordination with Streamlit team needed
- Can evolve independently

### Next Steps:
1. Choose preferred animation style from demo
2. Implement in CarbonButton.tsx
3. Add CSS animations to component
4. Update Python wrapper
5. Test and document

This keeps the feature self-contained within our component while providing a clean, intuitive API for users.
