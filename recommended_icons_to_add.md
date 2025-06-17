# Recommended Carbon Icons to Add to Streamlit Button Component

## Priority 1: Essential Data Visualization Icons

### Charts (Must-Have)
```python
# Basic charts
"chart--bar": "chart--bar.svg",
"chart--line": "chart--line.svg",
"chart--scatter": "chart--scatter.svg",
"chart--pie": "chart--pie.svg",
"chart--area": "chart--area.svg",
"chart--column": "chart--column.svg",

# Advanced charts
"chart--bubble": "chart--bubble.svg",
"chart--histogram": "chart--histogram.svg",
"chart--treemap": "chart--treemap.svg",
"chart--network": "chart--network.svg",
"chart--radar": "chart--radar.svg",
"chart--waterfall": "chart--waterfall.svg",
"chart--candlestick": "chart--candlestick.svg",  # Financial
"chart--heat-map": "heat-map.svg",
```

### Data & Analytics
```python
"analytics": "analytics.svg",
"data-analytics": "data-analytics.svg",
"dashboard": "dashboard.svg",
"data-table": "data-table.svg",
"data-view": "data--view.svg",
"data-set": "data--set.svg",
"data-vis-1": "data-vis--1.svg",
"data-vis-2": "data-vis--2.svg",
```

## Priority 2: Essential UI & Form Icons

### Input & Forms
```python
"calendar": "calendar.svg",
"time": "time.svg",
"dropdown": "dropdown.svg",
"checkbox": "checkbox.svg",
"checkbox-checked": "checkbox--checked.svg",
"radio-button": "radio-button.svg",
"filter": "filter.svg",
"filter-edit": "filter--edit.svg",
"search": "search.svg",
```

### Data Operations
```python
"export": "export.svg",
"download": "download.svg",
"cloud-upload": "cloud--upload.svg",
"cloud-download": "cloud--download.svg",
"data-share": "data-share.svg",
"data-backup": "data-backup.svg",
"filter-reset": "filter--reset.svg",
"upload": "upload.svg",
```

## Priority 3: Status & Feedback Icons

```python
"information": "information.svg",
"information-filled": "information--filled.svg",
"information-square": "information--square.svg",
"help": "help.svg",
"help-filled": "help--filled.svg",
"warning-alt": "warning--alt.svg",
"warning-filled": "warning--filled.svg",
"warning-square": "warning--square.svg",
"error": "error.svg",
"error-filled": "error--filled.svg",
"error-outline": "error--outline.svg",
```

## Priority 4: AI/ML & Advanced Features

```python
"ai": "AI.svg",
"ai-launch": "ai-launch.svg",
"ai-governance": "ai-governance--tracked.svg",
"machine-learning": "machine-learning.svg",
"cognitive": "cognitive.svg",
"bot": "bot.svg",
"chat-bot": "chat-bot.svg",
```

## Priority 5: Layout & View Icons

```python
"fit-to-screen": "fit-to-screen.svg",
"fit-to-width": "fit-to-width.svg",
"fit-to-height": "fit-to-height.svg",
"bottom-panel-open": "bottom-panel--open.svg",
"bottom-panel-close": "bottom-panel--close.svg",
"grid": "grid.svg",
"expand-all": "expand-all.svg",
"collapse-all": "collapse-all.svg",
"maximize": "maximize.svg",
"minimize": "minimize.svg",
```

## Priority 6: Settings & Configuration

```python
"settings": "settings.svg",
"settings-adjust": "settings--adjust.svg",
"tools": "calendar--tools.svg",
"gears": "gears.svg",
"build-tool": "build-tool.svg",
"api": "api.svg",
"api-1": "API--1.svg",
"api-key": "api--key.svg",
```

## Priority 7: Collaboration & Sharing

```python
"share": "share.svg",
"data-share": "data-share.svg",
"collaborate": "collaborate.svg",
"send": "send.svg",
"send-filled": "send--filled.svg",
"send-alt": "send--alt.svg",
"send-alt-filled": "send--alt--filled.svg",
"group": "group.svg",
"group-objects": "group-objects.svg",
"user-multiple": "user--multiple.svg",
```

## Implementation Categories Structure

```python
ICON_CATEGORIES = {
    "charts": {
        "title": "Charts & Graphs",
        "icons": ["chart--bar", "chart--line", "chart--scatter", "chart--pie", ...]
    },
    "data": {
        "title": "Data & Analytics",
        "icons": ["analytics", "dashboard", "data-table", "data-view", ...]
    },
    "forms": {
        "title": "Forms & Input",
        "icons": ["calendar", "dropdown", "checkbox", "radio-button", "filter", ...]
    },
    "operations": {
        "title": "Data Operations",
        "icons": ["export", "import", "cloud-upload", "cloud-download", ...]
    },
    "status": {
        "title": "Status & Feedback",
        "icons": ["information", "help", "notification", "pending", ...]
    },
    "ai": {
        "title": "AI & Machine Learning",
        "icons": ["ai", "ai-launch", "cognitive", "bot", ...]
    },
    "layout": {
        "title": "Layout & Views",
        "icons": ["maximize", "minimize", "side-panel-open", "grid", ...]
    },
    "settings": {
        "title": "Settings & Config",
        "icons": ["settings", "tools", "api", ...]
    },
    "collaboration": {
        "title": "Collaboration",
        "icons": ["share", "collaborate", "link", "send", ...]
    }
}
```

## Notes for Implementation

1. **File Verification**: All icons listed above have been verified to exist in the Carbon repository
2. **Naming Convention**: Follow the existing pattern of converting SVG names (e.g., `chart--bar.svg` → `"chart--bar"`)
3. **Category Organization**: Group icons logically to make them easy to discover
4. **Priority Implementation**: Start with Priority 1 & 2 as they provide the most value for typical Streamlit use cases
5. **Testing**: Ensure each icon renders correctly at different sizes (16, 20, 24, 32)

## Total New Icons: ~80-100
This would expand the current ~100 icons to approximately 180-200 icons, providing comprehensive coverage for most Streamlit use cases.
