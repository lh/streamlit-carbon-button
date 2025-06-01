import React from "react"
import { createRoot } from "react-dom/client"
import CarbonButton from "./CarbonButton"
import "./index.css"

// Component loaded
console.log("Carbon Button Component: Script loaded!")

// Debug logging
console.log("Carbon Button Component: Initializing...")
window.addEventListener('DOMContentLoaded', () => {
  console.log("DOM Content Loaded")
})

const rootElement = document.getElementById("root")
console.log("Root element:", rootElement)

if (rootElement) {
  const root = createRoot(rootElement)
  root.render(
    <React.StrictMode>
      <CarbonButton />
    </React.StrictMode>
  )
  console.log("Carbon Button Component: Rendered")
} else {
  console.error("Carbon Button Component: Root element not found!")
  // Try to create a fallback
  const fallback = document.createElement('div')
  fallback.textContent = 'ERROR: No root element found!'
  fallback.style.color = 'red'
  document.body.appendChild(fallback)
}