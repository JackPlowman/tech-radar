from logging import getLogger
from os import getenv

import pytest
from playwright.sync_api import Page

logger = getLogger(__name__)


@pytest.fixture
def project_url() -> str:
    """Fixture to provide the project URL."""
    url = getenv("PROJECT_URL")
    if not url:
        msg = "The environment variable 'PROJECT_URL' is not set. "
        raise ValueError(msg)
    return url


def test_title(page: Page, project_url: str) -> None:
    """Test the page title."""
    # Act
    page.goto(project_url)
    # Assert
    assert page.title() == "Jack Plowman's Tech Radar"


def test_theme_toggle(page: Page, project_url: str) -> None:
    """Test the theme toggle functionality."""
    # Act
    page.goto(project_url)
    # Assert
    assert page.locator("button#theme-toggle").is_visible()
    # Click the theme toggle button
    page.locator("button#theme-toggle").click()
    # Assert the theme has changed
    assert page.locator("body").get_attribute("class") == "dark-mode"
