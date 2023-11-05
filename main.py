from data_processing import get_adjectives
from html_exporter import html_export

if __name__ == '__main__':
    adjectives = get_adjectives()
    html_export(adjectives)
    print('Done!')