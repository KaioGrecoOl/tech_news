import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url: str) -> str:
    try:
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
        time.sleep(3)
        if response.status_code == 200:
            return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css(".entry-preview .cs-overlay-link::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css(".next.page-numbers::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    quotes = scrape_next_page_link("https://blog.betrybe.com/")

    # page_content = fetch("https://blog.betrybe.com/")
    # news = scrape_novidades(page_content)
