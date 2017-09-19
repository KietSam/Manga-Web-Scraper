import requests
import bs4


def get_soup_from_url(url):
    try:
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        return soup
    except:
        message = 'Couldn\'t get soup for this url: %s' % url
        raise
