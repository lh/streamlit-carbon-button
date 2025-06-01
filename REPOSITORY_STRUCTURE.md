# Repository Structure Plan

## Option 1: Two GitHub Repositories

### Repository 1: `streamlit-carbon-button-dev`
**Purpose**: Full development environment for customizing and building the component

```
streamlit-carbon-button-dev/
├── frontend/                    # React source code
│   ├── src/
│   │   ├── CarbonButton.tsx    # Main component
│   │   ├── index.tsx           # Entry point
│   │   └── index.css           # Styles
│   ├── package.json
│   ├── vite.config.ts
│   └── tsconfig.json
├── briquette/                  # Python package source
│   ├── __init__.py            # Python wrapper
│   └── frontend/              # Built files (git-ignored)
├── build.sh                    # Build script
├── setup.py                    # Python package setup
├── requirements.txt
├── README.md                   # Development documentation
├── CONTRIBUTING.md
├── LICENSE
└── examples/                   # All test files
    ├── test_basic.py
    ├── test_default_button.py
    ├── test_dynamic_default.py
    └── test_icon_only_default.py
```

### Repository 2: `streamlit-carbon-button`
**Purpose**: Simple, ready-to-use package for end users

```
streamlit-carbon-button/
├── streamlit_carbon_button/    # Renamed from briquette
│   ├── __init__.py            # Python wrapper
│   └── frontend/              # Pre-built React files
│       ├── index.html
│       └── static/
│           ├── js/
│           └── css/
├── setup.py                    # Simplified setup
├── requirements.txt            # Just needs streamlit
├── README.md                   # User documentation
├── LICENSE
└── examples/
    └── simple_example.py       # Basic usage example
```

## Option 2: Single Repo + PyPI

### Repository: `streamlit-carbon-button`
```
streamlit-carbon-button/
├── frontend/                    # React source
├── streamlit_carbon_button/     # Python package
├── build.sh
├── setup.py
├── pyproject.toml              # Modern Python packaging
├── README.md
├── LICENSE
├── .github/
│   └── workflows/
│       └── publish.yml         # Auto-publish to PyPI
└── examples/
```

Users install with:
```bash
pip install streamlit-carbon-button
```

## Recommended File Distribution

### For Development Repository:
- All source files
- Build tools and configurations  
- Development dependencies
- Test suites
- Documentation for contributors

### For Distribution Repository/Package:
- Pre-built component files only
- Minimal Python wrapper
- Simple examples (1-2 files)
- User-focused README
- No build dependencies

## Key Differences:
1. **Distribution repo has no Node.js/React dependencies**
2. **Distribution repo includes pre-built files in git**
3. **Development repo has comprehensive tests and docs**
4. **Distribution repo has minimal, user-focused documentation**