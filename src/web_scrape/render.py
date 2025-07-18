import time
from urllib.parse import urlparse

from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

from web_scrape.tools import sanitize_url


def render_page(url: str, wait_time: int = 3) -> str:
    """Use Selenium to render a dynamic webpage and return the HTML."""
    sanitized_url = sanitize_url(url)

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    html = ""

    try:
        driver = webdriver.Chrome(options=options)
        try:
            driver.get(sanitized_url)
            time.sleep(wait_time)
            html = driver.page_source
        except Exception as e:
            logger.error(f"Failed to render page content for {sanitized_url}: {e}")
        finally:
            driver.quit()
    except WebDriverException as e:
        logger.error(f"Could not initialize WebDriver: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

    return html
