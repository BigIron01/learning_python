import requests
import os
from string import punctuation
from urllib.parse import urljoin

from bs4 import BeautifulSoup


url = "https://www.nature.com/nature/articles"
page_n = int(input())
article_kind = input()
for _ in range(1, page_n + 1):
    search_params = {"sort": "PubDate", "year": "2020", "page": _}
    base_r = requests.get(url, params=search_params)
    base_soup = BeautifulSoup(base_r.content, "html.parser")
    saved_files = []
    folder_name = "Page_" + (str(_))

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    article_list = base_soup.find_all(attrs={"data-track-action": "view article"})

    for article in article_list:
        article_type = article.findParent("article").find(attrs={"class": "c-meta__type"})
        if article_type.find(text=article_kind):
            article_title = "".join([letter for letter in article.text if letter not in punctuation]).replace(" ", "_")
            article_r = requests.get(urljoin(url, article["href"]))
            article_data = BeautifulSoup(article_r.content, "html.parser")
            article_soup = article_data.find(attrs={"class": "c-article-body"}).text
            with open(f"{os.path.abspath(folder_name)}/{article_title}.txt", "wt", encoding="utf-8") as file:
                file.write(article_soup)
                saved_files.append(f"{article_title}.txt")
