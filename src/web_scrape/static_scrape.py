import httpx
from loguru import logger

from web_scrape.tools import sanitize_url, extract_visible_text


def fetch_static_html(url: str, timeout: int = 10) -> str:
    """Fetch HTML from a static web page using httpx with redirect support."""
    sanitized = sanitize_url(url)
    try:
        with httpx.Client(follow_redirects=True, timeout=timeout) as client:
            response = client.get(sanitized)
            response.raise_for_status()
            return response.text
    except httpx.HTTPStatusError as e:
        return f"[ERROR] HTTP error for {sanitized}: {e.response.status_code} {e.response.reason_phrase}"
    except httpx.RequestError as e:
        return f"[ERROR] Failed to connect to {sanitized}: {str(e)}"
    except Exception as e:
        return f"[ERROR] Unexpected error: {str(e)}"


def scrape_static_text(url: str) -> str:
    """Fetch and extract visible text from a static HTML page."""
    html = fetch_static_html(url)
    if html.startswith("[ERROR]"):
        return html
    return extract_visible_text(html)
