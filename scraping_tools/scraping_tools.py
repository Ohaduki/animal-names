import requests
from bs4 import BeautifulSoup


def get_page(url:str) -> BeautifulSoup:
    """
    Fetches a web page and returns its content as a BeautifulSoup object.

    Parameters:
        url (str): The URL of the web page to fetch.

    Returns:
        soup: A BeautifulSoup object representing the parsed web page.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_src(url:str) -> str:
    """
    Gets the image src of a given wikipedia article. Includes cases for all animals on the list.

    Parameters:
        url (str): The URL of the animal's page to fetch.

    Returns:
        src: The animal's image src.
    """
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


def get_image(url:str, name:str) -> str:
    """
    Downloads the image from a given src and also returns the file extension from the url.

    Parameters:
        url (str): The URL of the image.

    Returns:
        extenstion: the file extension of the file downloaded. Also saves the file to tmp/{name}
    """
    extension = url.split('.')[-1]
    headers = {'User-Agent': 'Ohad/0.0, (ohad.licht@gmail.com)'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(f'tmp/{name}.{extension}', 'wb') as file:
            file.write(response.content)
    else:
        print(f'Error: {response.status_code}')
    return extension