from loguru import logger

from web_scrape.static_scrape import scrape_static_text
from web_scrape.render import render_page
from web_scrape.tools import extract_visible_text


def smart_scrape(url: str) -> str:
    """
    Try static scrape first; if it fails or returns no content,
    fall back to Selenium dynamic rendering.
    """
    logger.info(f"Attempting static scrape for: {url}")
    text = scrape_static_text(url)
    logger.debug(f"{text = }")

    if not text.strip() or text.startswith("[ERROR]"):
        logger.info(
            f"Static scrape failed or returned empty. Falling back to dynamic render."
        )
        html = render_page(url)
        text = extract_visible_text(html)
        logger.debug(f"{text = }")

    return text or ""
