# Migration Plan: CRA to Vite for streamlit-carbon-button

## Overview
This document outlines the migration from Create React App (CRA) to Vite for the streamlit-carbon-button component. Vite is the recommended modern build tool by the React team after CRA's deprecation.

## Why Vite?
- **Recommended by React team** as a CRA replacement
- **Used by Streamlit** in their official component template
- **Faster builds** (10-100x faster HMR)
- **Smaller bundle sizes**
- **Better TypeScript support**
- **Active maintenance** and growing ecosystem

## Current Setup Analysis
- **Framework**: React 18.2.0 with TypeScript
- **Build Tool**: Create React App (react-scripts 5.0.1)
- **Key Dependencies**:
  - streamlit-component-lib: ^2.0.0
  - React/React-DOM: ^18.2.0
  - TypeScript: ^4.9.0
- **Component Structure**: Single CarbonButton.tsx component with inline styles
- **Features to Preserve**:
  - Dark mode detection
  - SVG icon injection
  - Carbon Design System styling
  - Streamlit communication (setComponentValue, setFrameHeight)
  - Hover/active states with color transitions

## Migration Steps

### Phase 1: Preparation
1. **Backup current working build**
   ```bash
   cp -r frontend/build frontend/build.cra-backup
   cp -r briquette/frontend briquette/frontend.cra-backup
   git add frontend/build.cra-backup briquette/frontend.cra-backup
   git commit -m "Backup CRA build before migration"
   ```

2. **Document current behavior**
   - Screenshot all button states (rest, hover, active)
   - Record performance metrics
   - Note bundle sizes

### Phase 2: Test Suite Creation
Create automated tests to ensure functionality preservation (see test_suite_migration.py).

### Phase 3: Vite Setup
1. **Create new Vite config**
2. **Install Vite dependencies**
3. **Migrate build scripts**
4. **Update TypeScript config**
5. **Adjust import paths if needed**

### Phase 4: Validation
1. **Run test suite**
2. **Compare bundle sizes**
3. **Visual regression testing**
4. **Performance comparison**

### Phase 5: Cleanup
1. **Remove CRA dependencies**
2. **Update documentation**
3. **Update CI/CD if applicable**

## Migration Checklist

- [ ] Backup current build
- [ ] Create test suite
- [ ] Set up Vite project structure
- [ ] Migrate TypeScript config
- [ ] Update package.json scripts
- [ ] Migrate component code
- [ ] Test development mode
- [ ] Test production build
- [ ] Run visual regression tests
- [ ] Run functional tests
- [ ] Verify Streamlit integration
- [ ] Update documentation
- [ ] Remove CRA dependencies
- [ ] Update GitHub workflows (if any)
- [ ] Test deployment to Streamlit Cloud

## Risk Mitigation

1. **Rollback Plan**: Keep CRA backup until Vite version is proven stable
2. **Gradual Migration**: Test with small subset of users first
3. **Version Pinning**: Pin all Vite-related dependencies initially
4. **Compatibility Testing**: Test across different Streamlit versions

## Timeline Estimate

- Phase 1 (Preparation): 1 day
- Phase 2 (Test Suite): 2-3 days
- Phase 3 (Vite Setup): 1-2 days
- Phase 4 (Validation): 1-2 days
- Phase 5 (Cleanup): 1 day

**Total: 6-10 days** for complete migration with comprehensive testing
