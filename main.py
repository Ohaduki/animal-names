from data_processing.data_processing import get_adjectives
from html_exporter.html_exporter import html_export

if __name__ == '__main__':
    print('Fetching data...')
    adjectives = get_adjectives()
    print('Exporting HTML...')
    html_export(adjectives)
    print('Done!')