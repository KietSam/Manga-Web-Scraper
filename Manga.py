import requests
import bs4

class Manga:
    def __init__(self, url):
        self.url = url
        self.chapter_dict = self.get_all_chapter_urls()

    def get_soup_from_url(self, url):
        try:
            res = requests.get(url)
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            return soup
        except:
            message = 'Couldn\'t get soup for this url: %s' % url
            raise

    def get_all_chapter_urls(self):
        soup = self.get_soup_from_url(self.url)
        chapters = soup.find_all('a', class_="list-group-item")
        chapter_dict = {}
        for chapter in chapters:
            chapter_num = float(chapter.get('chapter'))
            chapter_url = chapter.get("href")
            chapter_dict[chapter_num] = chapter_url
        return chapter_dict
