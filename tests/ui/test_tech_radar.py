from logging import getLogger

from playwright.sync_api import Page

logger = getLogger(__name__)

PAGE_URL = "https://jackplowman.github.io/tech-radar/"

def test_title(page: Page) -> None:
    """Test the page title."""
    # Act
    page.goto(PAGE_URL)
    # Assert
    assert page.title() == "Jack Plowman's Tech Radar"
