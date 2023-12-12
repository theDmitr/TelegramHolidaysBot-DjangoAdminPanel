from datetime import datetime

import requests
from bs4 import BeautifulSoup

holidays_site_url = 'https://www.rusevents.ru/date/'


def remove_all_tags(soup: BeautifulSoup, tags: list):
    for data in soup(tags):
        data.decompose()


def get_holidays(date: datetime.date = datetime.today().date()):
    str_date = date.strftime("%d.%m")
    page_str = requests.get(holidays_site_url + str_date).text
    soup = BeautifulSoup(page_str, 'html.parser')
    remove_all_tags(soup, ['span'])
    titles = soup.find_all(attrs={'class': 'title'})
    return [title.text.strip() for title in titles]
