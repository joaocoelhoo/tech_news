import requests
import time
from parsel import Selector


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get("https://www.betrybe.com/",
                                timeout=3,
                                headers={"user-agent": "Fake user-agent"})
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    list_content = []
    for content in selector.css("div.entry-thumbnail"):
        url = content.css("a::attr(href)").get()
        list_content.append(url)

    return list_content


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_url = selector.css("a.next::attr(href)").get()

    return next_url


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("head > link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    date = selector.css("li.meta-date::text").get()
    author = selector.css("span.author > a::text").get()
    comments = selector.css("ol.comment-list li").getall()
    summary = selector.css(
        "div.entry-content > p:first-of-type *::text").getall()
    tags = selector.css("section.post-tags a::text").getall()
    category = selector.css("div.meta-category span.label::text").get()
    print(category)
    return {
        "url": url,
        "title": title.strip(),
        "timestamp": date,
        "writer": author,
        "comments_count": len(comments),
        "summary": ''.join(summary).strip(),
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
