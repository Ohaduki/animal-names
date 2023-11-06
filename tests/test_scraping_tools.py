from scraping_tools.scraping_tools import get_page, get_src, get_image

from bs4 import BeautifulSoup

class TestGetPage:

    def setup_method(self):
        self.soup = get_page('https://en.wikipedia.org/wiki/List_of_animal_names')
    
    def test_function_works(self):
        assert self.soup
    
    def test_returns_soup(self):
        assert type(self.soup) == BeautifulSoup


class TestGetSrc:

    def test_infobox(self):
        assert get_src('https://en.wikipedia.org/wiki/Anteater') == "//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Tamandu%C3%A1-bandeira_no_Parque_Nacional_da_Serra_da_Canastra_%28cropped%29.jpg/220px-Tamandu%C3%A1-bandeira_no_Parque_Nacional_da_Serra_da_Canastra_%28cropped%29.jpg"
    
    def test_figure(self):
        assert get_src('https://en.wikipedia.org/wiki/Crow') == "//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Corvus_corone_-near_Canford_Cliffs%2C_Poole%2C_England-8.jpg/220px-Corvus_corone_-near_Canford_Cliffs%2C_Poole%2C_England-8.jpg"
    
    def test_multiimageinner(self):
        assert get_src('https://en.wikipedia.org/wiki/Black_panther') == "//upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Black_Panther_-_India.jpg/200px-Black_Panther_-_India.jpg"


class TestGetImage:

    def test_jpg(self):
        assert get_image('https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Black_Panther_-_India.jpg/400px-Black_Panther_-_India.jpg', "panther") == 'jpg'

    def test_png(self):
        assert get_image('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Chinese%2Bamerican_alligators.png/440px-Chinese%2Bamerican_alligators.png', "alligator") == 'png'