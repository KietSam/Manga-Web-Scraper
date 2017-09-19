import Constants
from Souper import get_soup_from_url
from Chapter import Chapter

class Manga:
    def __init__(self, url):
        self.url = url
        self._process_page()

    def _process_page(self):
        soup = get_soup_from_url(self.url)
        chapter_soups = soup.find_all('a', class_="list-group-item")
        chapters = []
        for chapter_soup in chapter_soups:
            chapter_num = float(chapter_soup.get('chapter'))
            chapter = Chapter(chapter_num, Constants.DOMAIN_URL + chapter_soup.get("href"))
            chapters.append(chapter)
        chapters.sort(key=lambda x: x.chapter_num)
        self.chapters = chapters
