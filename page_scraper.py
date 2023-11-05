import requests
from bs4 import BeautifulSoup

def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_adjectives():
    adjectives = {}
    soup = get_page('https://en.wikipedia.org/wiki/List_of_animal_names')
    wiki_tables = soup.find_all('table', class_='wikitable')
    rows = wiki_tables[1].find_all('tr')
    for row in rows[1:]:
        cells = row.find_all('td')
        if len(cells) > 1:
            if len(cells[5].text) > 1:
                if cells[5].text not in adjectives.keys():
                    adjectives[cells[5].text] = [cells[0].text]
                else:
                    adjectives[cells[5].text].append(cells[0].text)
    return adjectives

print(get_adjectives())
            


get_adjectives()