# GitHub Copilot Instructions for Tech Radar

## Project Overview

This is a personal tech radar visualization project built as a static GitHub Pages site. It displays technologies across quadrants (Tools, Platforms, Languages, Techniques) and rings (Experienced, Trial, Watch, Maintain) using D3.js and the Zalando tech radar library.

## Architecture & Key Components

- **Static Site**: `github-pages/` contains the complete web application
  - `index.html`: Main page with D3.js radar visualization and theme switching
  - `config.json`: **Primary data file** - all radar entries in structured JSON format
  - `radar.css` & `dark-mode.css`: Styling with theme support
- **Testing**: `tests/` directory with Playwright E2E tests using UV/Python packaging
- **Build System**: Just command runner with modular justfiles (`Justfile` + `tests/tests.just`)

## Critical Data Structure

All radar content is defined in `github-pages/config.json`:

```json
{
  "quadrant": 2, // 0=Tools, 1=Platforms, 2=Languages, 3=Techniques
  "ring": 0, // 0=Experienced, 1=Trial, 2=Watch, 3=Maintain
  "label": "Python",
  "active": true,
  "moved": 0, // 0=No change, 1=Inward, 2=Outward
  "link": "https://www.python.org/"
}
```

## Development Workflows

### Local Development

```bash
# Start dev server (serves github-pages/ directory)
python3 -m http.server
# Navigate to http://localhost:8000/github-pages/
```

### Testing

```bash
# Install test dependencies
just tests::install

# Run E2E tests against local or deployed site
just tests::run                           # Uses DEFAULT_PROJECT_URL
just tests::run "http://localhost:8000/github-pages/" # Custom URL
just tests::run-ci chromium               # CI browser-specific testing
```

### Code Quality (Pre-commit via Prek)

```bash
# Install git hooks
just install-git-hooks

# Manual checks (same as pre-commit)
just prettier-check        # Format checking
just gitleaks-detect       # Secret scanning
just zizmor-check         # GitHub Actions security
just pinact-check         # GitHub Actions pinning
```

## Project-Specific Patterns

1. **Modular Just Commands**: Uses `mod tests 'tests/tests.just'` pattern - call test commands with `just tests::<command>`

2. **UV Python Management**: Tests use UV for fast dependency resolution, not pip/poetry
   - `pyproject.toml` in tests/ subdirectory
   - `uv sync --all-extras` for installation

3. **Reusable Workflows**: CI uses centralized workflows from `JackPlowman/reusable-workflows` with SHA pinning

4. **Multi-Tool Security**: Combines gitleaks (secrets), zizmor (Actions security), and pinact (dependency pinning)

5. **GitHub Pages Deployment**: Direct static hosting from `github-pages/` directory, no build step required

## Common Tasks

- **Add Technology**: Edit `github-pages/config.json` entries array with correct quadrant/ring values
- **Theme Changes**: Modify `dark-mode.css` and `radar.css`, test with theme toggle button
- **Test Updates**: Playwright tests focus on core functionality (title, theme toggle, radar rendering)
- **CI Debugging**: Check both common-code-checks (reusable workflow) and Python-specific jobs

## Integration Points

- **GitHub Pages**: Auto-deploys from `github-pages/` directory on main branch
- **Zalando Tech Radar**: External library loaded via CDN (`radar-0.8.js`)
- **D3.js v4**: Specific version dependency for radar visualization
- **Playwright**: Browser testing across Chromium/Firefox/WebKit
