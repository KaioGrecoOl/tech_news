from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    search_info_news = search_news(
        {"title": {"$regex": f"{title}", "$options": "i"}}
    )
    response = []
    for data in search_info_news:
        response.append(
            (data["title"], data["url"]),
        )
    return response


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
