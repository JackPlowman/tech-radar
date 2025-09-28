from logging import getLogger
from os import getenv
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

SNAPSHOT_DIR = Path(__file__).parent / "__snapshots__"

logger = getLogger(__name__)


@pytest.fixture
def project_url() -> str:
    """Fixture to provide the project URL."""
    url = getenv("PROJECT_URL")
    if not url:
        msg = "The environment variable 'PROJECT_URL' is not set. "
        raise ValueError(msg)
    return url


@pytest.fixture
def radar_page(page: Page, project_url: str) -> Page:
    """A Playwright page primed with deterministic settings for the radar."""
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
    return page


def test_title(radar_page: Page) -> None:
    """Test the page title."""
    assert radar_page.title() == "Jack Plowman's Tech Radar"


def test_theme_toggle(radar_page: Page) -> None:
    """Test the theme toggle functionality."""
    assert radar_page.locator("button#theme-toggle").is_visible()
    # Click the theme toggle button
    radar_page.locator("button#theme-toggle").click()
    # Assert the theme has changed
    assert radar_page.locator("body").get_attribute("class") == "dark-mode"


def test_radar_visual_regression(radar_page: Page) -> None:
    """Ensure the radar page maintains its visual appearance."""
    snapshot_path = SNAPSHOT_DIR / "tech-radar-home.aria"
    expected_snapshot = snapshot_path.read_text(encoding="utf-8")
    radar_page.wait_for_timeout(500)
    expect(radar_page.locator("body")).to_match_aria_snapshot(expected_snapshot)
