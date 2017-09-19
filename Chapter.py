import Constants
from Souper import get_soup_from_url


class Chapter:
    def __init__(self, url):
        self._parse_url(url)

    def _parse_url(self, url):
        # Check domain url
        domain_url = url[:Constants.DOMAIN_URL.__len__()]
        if (domain_url != Constants.DOMAIN_URL):
            raise Exception("Wrong domain url detected: " + domain_url)

        # Set "single page" to "all pages"
        url = url.replace(Constants.SINGLE_FIRST_PAGE_SUFFIX, Constants.ALL_PAGES_SUFFIX)
        self.url = url

        url = url.replace(".html", "")
        split = url.rsplit('-')
        length = len(split)

        second_to_last = split[length - 2]
        if (second_to_last == "chapter"):
            self.chapter_num = float(split[length - 1])
            self.season_num = 1
            return

        fourth_to_last = split[length - 4]
        if (second_to_last == "index" and fourth_to_last == "chapter"):
            self.chapter_num = float(split[length - 3])
            self.season_num = int(split[length - 1])
            return

        raise Exception("Unexpectedly reached the end of this method.")


    def get_image_urls(self):
        soup = get_soup_from_url(self.url)
        image_soups = soup.find_all("div", class_="fullchapimage")
        image_urls = []
        for image_soup in image_soups:
            # print(image_soup.img.get("src"))
            image_urls.append(image_soup.img.get("src"))
        self.image_urls = image_urls

    def download_chapter(self):
        if season_number > 1:
            chapter_name = '%s S%d Ch. %g' % (manga_name, season_number, chapter_number)
        else:
            chapter_name = '%s Ch. %g' % (manga_name, chapter_number)

