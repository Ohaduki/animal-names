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
                if cells[5].text not in adjectives.keys():
                    adjectives[cells[5].text] = [(name, extension)]
                else:
                    adjectives[cells[5].text].append((name, extension))
    return adjectives

def get_src(url):
    soup = get_page(url)
    infobox = soup.find('table', class_='infobox')
    if infobox:
        image = infobox.find('img')
        if image:
            return image['src']
    figure = soup.find('figure')
    if figure:
        image = figure.find('img')
        if image:
            return image['src']
    multiimageinner = soup.find('div', class_='multiimageinner')
    if multiimageinner:
        image = multiimageinner.find('img')
        if image:
            return image['src']

def get_image(url, name):
    extension = url.split('.')[-1]
    headers = {'User-Agent': 'Ohad/0.0, (ohad.licht@gmail.com)'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(f'tmp/{name}.{extension}', 'wb') as file:
            file.write(response.content)
    else:
        print(f'Error: {response.status_code}')
    return extension



def html_export(adjectives):
    body = ""

    for adjective in adjectives.keys():
        body += f"<h1>{adjective}</h1>"
        body += "<ul>"
        for name in adjectives[adjective]:
            body += f"<li>{name[0]}</li>"
            body += f"<img src='tmp/{name[0]}.{name[1]}'/>"
        body += "</ul>"
    
    html = f"""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
            {body}
            </body>
        </html>
    """

    with open('index.html', 'w') as file:
        file.write(html)


html_export(get_adjectives())