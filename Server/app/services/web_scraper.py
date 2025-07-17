import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

def scrape_static_content(url: str) -> str:
    """Scrapes the content from a static website."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        # This is a simple example. You will need to implement more
        # sophisticated logic to extract the relevant content from the page.
        return soup.get_text()
    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return ""

def scrape_dynamic_content(url: str) -> str:
    """Scrapes the content from a dynamic (JavaScript-rendered) website."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            page.goto(url)
            # This is a simple example. You may need to wait for specific
            # elements to load before getting the content.
            content = page.content()
            soup = BeautifulSoup(content, "html.parser")
            return soup.get_text()
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return ""
        finally:
            browser.close()
