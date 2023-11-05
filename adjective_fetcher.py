from bs4 import BeautifulSoup

from adjective_fetcher import get_page

def get_adjectives():
    adjectives = {}
    soup = get_page('https://en.wikipedia.org/wiki/List_of_animal_names')
    wiki_tables = soup.find_all('table', class_='wikitable')
    rows = wiki_tables[1].find_all('tr')
    print(rows[0])
    print("------")
    print(rows[1])


get_adjectives()