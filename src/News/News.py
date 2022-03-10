import requests
from random import randrange

API_KEY = '96ab9c0a0ff64e8f981301b8f598140f'
USAGE = 'News.py <query> <searchIn> <language> <category>'
URL = 'https://newsapi.org/v2/everything'

LANG_OPT = ["ar", "de", "en", "es", "fr", "he", "it", "nl", "no", "pt", "zu", "se", "ud", "zh"]


def orderContent(article):
    returnContent = f'''"*{article.get("title")}*"
{article.get("url")}'''
    return returnContent

def getNews(query, searchIn, language):
    url = f"{URL}?q={query}&searchIn{searchIn}&language={language}&sortBy=publishedAt&apiKey={API_KEY}"
    r = requests.request("GET", url)
    return orderContent(r.json().get("articles")[randrange(len(r.json().get("articles")))])

if __name__ == '__main__':
    print(getNews("Python", "title", "es", "popularity"))