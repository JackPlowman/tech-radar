from __future__ import annotations

import os
from pathlib import Path

from playwright.sync_api import sync_playwright


def main() -> None:
    """Generate a snapshot of the tech radar page for visual regression testing."""
    project_url = os.environ.get("PROJECT_URL")
    if not project_url:
        msg = (
            "The environment variable 'PROJECT_URL' "
            "must be set to capture the snapshot."
        )
        raise RuntimeError(msg)

    snapshot_path = Path(__file__).parent / "__snapshots__" / "tech-radar-home.aria"
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.add_init_script(
            """
            (() => {
                window.localStorage.setItem('theme', 'light');
                window.matchMedia = (query) => ({
                    matches: false,
                    media: query,
                    onchange: null,
                    addListener: () => {},
                    removeListener: () => {},
                    addEventListener: () => {},
                    removeEventListener: () => {},
                    dispatchEvent: () => false,
                });
            })();
            """,
        )
        page.set_viewport_size({"width": 1450, "height": 1000})
        page.goto(project_url, wait_until="networkidle")
        page.wait_for_selector("svg#radar")
        page.add_style_tag(
            content="""
            *, *::before, *::after {
                transition-duration: 0s !important;
                animation-duration: 0s !important;
                animation-delay: 0s !important;
            }
            """,
        )
        page.wait_for_timeout(500)
        snapshot = page.locator("body").aria_snapshot()
        browser.close()

    snapshot_path.write_text(snapshot, encoding="utf-8")


if __name__ == "__main__":
    main()
