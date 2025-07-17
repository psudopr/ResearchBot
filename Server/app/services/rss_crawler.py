import feedparser
from app.core.exceptions import CrawlingError

def crawl_rss_feed(feed_url: str) -> list[dict]:
    """Crawls an RSS feed and returns a list of entries."""
    try:
        feed = feedparser.parse(feed_url)
        if feed.bozo:
            raise CrawlingError(url=feed_url, message=f"Malformed feed: {feed.bozo_exception}")
        return feed.entries
    except Exception as e:
        raise CrawlingError(url=feed_url, message=str(e))
