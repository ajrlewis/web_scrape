import sys

from loguru import logger

from web_scrape.smart_scrape import smart_scrape


def main(url: str):
    text = smart_scrape(url)
    logger.info(text)


if __name__ == "__main__":
    url = sys.argv[1]
    main(url)
