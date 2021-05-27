import requests
from requests import get
from bs4 import BeautifulSoup

comic_info = {
    'title': " ",
    'status': " ",
    'date': 0,
    'views': 0,
    'rating': 0
}

class Issue:
    def __init__(self, name, issue_number):
        self.name = name
        self.issue_number = issue_number


def get_info(name):
    url = 'https://readcomicsonline.ru/comic/'+name
    response = get(url)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)

    info_container = html_soup.find_all('dd')

    comic_info[1] = info_container[1].text #status
    comic_info[2] = info_container[2].text #date
    comic_info[3] = info_container[5].text #views
    comic_info[4] = info_container[6].text #rating

    info_container = html_soup.find_all('h2', class_ = 'listmanga-header')
    
    comic_info[0] = info_container[0].text #title
    
    return comic_info