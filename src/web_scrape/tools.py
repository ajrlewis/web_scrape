import time
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from loguru import logger


def sanitize_url(url: str) -> str:
    """Ensure the URL starts with https://"""
    parsed = urlparse(url)
    if not parsed.scheme:
        return "https://" + url
    logger.debug(f"Sanitized URL: {url}")
    return url


def extract_visible_text(html: str) -> str:
    """Extracts visible text from HTML content."""
    soup = BeautifulSoup(html, "html.parser")

    # Remove scripts, styles, and other non-visible elements
    for tag in soup(["script", "style", "head", "meta", "[document]", "noscript"]):
        tag.decompose()

    # Get text and clean it
    text = soup.get_text(separator=" ", strip=True)

    # Optionally remove extra whitespace
    cleaned_text = " ".join(text.split())

    return cleaned_text
