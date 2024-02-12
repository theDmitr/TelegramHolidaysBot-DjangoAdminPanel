import requests
from bs4 import BeautifulSoup

holidays_site_url = 'https://celebratoday.com/ru'


def remove_all_tags(soup: BeautifulSoup, tags: list):
    for data in soup(tags):
        data.decompose()


def get_holidays():
    page_str = requests.get(holidays_site_url).text
    soup = BeautifulSoup(page_str, 'html.parser')
    spans = soup.find_all('section', {'class': 'grid gap-8'})[0].find_all('span', {'class': 'text-xl font-bold hover:underline'})
    return [s.get_text() for s in spans]
