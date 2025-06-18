from logging import getLogger
from os import getenv

from playwright.sync_api import Page

logger = getLogger(__name__)

PROJECT_URL = getenv("PROJECT_URL")
if not PROJECT_URL:
    msg = "The environment variable 'PROJECT_URL' is not set. "
    raise ValueError(msg)


def test_title(page: Page) -> None:
    """Test the page title."""
    # Act
    page.goto(PROJECT_URL)
    # Assert
    assert page.title() == "Jack Plowman's Tech Radar"
