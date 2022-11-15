from tech_news.database import search_news
import datetime


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
    try:
        time_stamp = datetime.date.fromisoformat(date).strftime("%d/%m/%Y")
        data_info = search_news({"timestamp": {"$regex": time_stamp}})
    except ValueError:
        raise ValueError("Data inválida")
    return [(item["title"], item["url"]) for item in data_info]


# Requisito 8
def search_by_tag(tag):
    search_info_tag = search_news(
        {"tags": {"$elemMatch": {"$regex": f"{tag}", "$options": "i"}}}
    )
    response = []
    for data in search_info_tag:
        response.append(
            (data["title"], data["url"]),
        )
    return response


# Requisito 9
def search_by_category(category):
    search_info_category = search_news(
      {"category": {"$regex": f"{category}", "$options": "i"}}
    )
    response = []
    for data in search_info_category:
        response.append(
          (data["title"], data["url"])
        )
    return response
