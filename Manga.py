import Constants
from Chapter import Chapter
from joblib import Parallel, delayed
from Souper import get_soup_from_url

class Manga:
    def __init__(self, url):
        self.url = url

    def get_chapter_urls(self):
        soup = get_soup_from_url(self.url)
        chapter_soups = soup.find_all('a', class_="list-group-item")
        chapter_urls = []
        for chapter_soup in chapter_soups:
            chapter_urls.append(Constants.DOMAIN_URL + chapter_soup.get("href"))
        chapter_urls.reverse()
        return chapter_urls

    def download_manga(self, save_path):
        chapter_urls = self.get_chapter_urls()
        for chapter_url in chapter_urls:
            self._download_chapter(save_path, chapter_url)

    def parallel_download_manga(self, save_path):
        chapter_urls = self.get_chapter_urls()
        Parallel(n_jobs=6)(delayed(self._download_chapter)(save_path, chapter_url) for chapter_url in chapter_urls)

    def _download_chapter(self, save_path, chapter_url):
        current_chapter = Chapter(chapter_url)
        print("Downloading", current_chapter.__str__())
        current_chapter.download_chapter(save_path)
