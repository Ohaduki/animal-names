from scraping_tools import get_page, get_src, get_image


def get_adjectives() -> dict[str, list[tuple[str, str]]]:
    """
    Fetches the list of animal names from Wikipedia and returns a dict of adjectives, animals and image extensions.

    Returns:
        Adjectives: A dict of each adjective in the wikipedia table, containing a list of (name, key) tuples for each animal with this adjective.
    """
    adjectives = {}
    soup = get_page('https://en.wikipedia.org/wiki/List_of_animal_names')
    wiki_tables = soup.find_all('table', class_='wikitable')
    rows = wiki_tables[1].find_all('tr')
    for row in rows[1:]:
        cells = row.find_all('td')
        if len(cells) > 1:
            if len(cells[5].text) > 1:
                name = cells[0].find('a').text.replace("/", " or ")
                ref = cells[0].find('a')['href']
                if ref.startswith('/'):
                    url = f"https://en.wikipedia.org{ref}"
                else:
                    url = f"https://en.wikipedia.org/"
                try:
                    extension = get_image("https:" + get_src(url), name)
                except Exception as e:
                    print(f'Error: {name}')
                    print(cells[0].find('a')['href'])
                    print(url)
                    print(get_src(url))
                    print(e)
                for adjective in filter(lambda x: isinstance(x, str), cells[5].contents):
                    if adjective not in adjectives.keys():
                        adjectives[adjective] = [(name, extension)]
                    else:
                        adjectives[adjective].append((name, extension))
    return adjectives