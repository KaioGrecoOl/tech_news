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
def scrape_noticia(html_content: str) -> list:
    selector = Selector(html_content)

    news_details = {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("a.url.fn.n::text").get(),
        "comments_count": len(
            selector.css("ol.coment-list a::attr(href)").getall()),
        "summary": selector.xpath("string(//p)").get().strip(),
        "tags": selector.css("section.post-tags > ul > li > a::text").getall(),
        "category": selector.css("a.category-style > span.label::text").get(),
    }

    return news_details


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
