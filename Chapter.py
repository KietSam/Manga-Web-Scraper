import os
import Constants

from Souper import get_soup_from_url
from urllib.request import urlretrieve


class Chapter:
    def __init__(self, url):
        self._parse_url(url)

    def _parse_url(self, url):
        # Check starting url
        starting_url = url[:Constants.DOMAIN_URL.__len__() + Constants.READ_CHAPTER_EXT.__len__()]
        if (starting_url != Constants.DOMAIN_URL + Constants.READ_CHAPTER_EXT):
            print(starting_url)
            raise Exception("Wrong starting url detected: " + starting_url)

        # Set "single page" to "all pages"
        url = url.replace(Constants.SINGLE_FIRST_PAGE_SUFFIX, Constants.ALL_PAGES_SUFFIX)

        # "http://mangaseeonline.us/read-online/One-Piece-chapter-878-page-1.html"
        # -> "One-Piece-chapter-878-page-1.html"
        manga_name = url[Constants.DOMAIN_URL.__len__() + Constants.READ_CHAPTER_EXT.__len__():]

        # "One-Piece-chapter-878-page-1.html"
        # -> "One-Piece" -> "One Piece"
        manga_name = manga_name[:manga_name.index("-chapter")].replace('-', ' ')

        self.url = url
        self.manga_name = manga_name

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
        return image_urls

    def download_chapter(self, save_path):
        save_path = self._add_end_slash(save_path)
        if self.season_num > 1:
            chapter_name = '%s S%d Ch. %g' % (self.manga_name, self.season_num, self.chapter_num)
        else:
            chapter_name = '%s Ch. %g' % (self.manga_name, self.chapter_num)

        chapter_path = save_path + '%s/%s' % (self.manga_name, chapter_name)
        if not os.path.exists(chapter_path):
            try:
                os.makedirs(chapter_path)
            except:
                message = 'Couldn\'t make folder for "%s" (%s)' % (chapter_name, self.url)
                return 0

        page_num = 1
        image_urls = self.get_image_urls()
        for image_url in image_urls:
            file_name = '%s page %d' % (chapter_name, page_num)
            if not os.path.isfile('%s/%s.png' % (chapter_path, file_name)):
                try:
                    file_path = '%s/%s.png' % (chapter_path, file_name)
                    urlretrieve(image_url, file_path)
                    print("Downloaded", file_name)
                except:
                    message = 'Couldn\'t download %s\n in this chapter: %s' % (image_url, chapter_name)
                    print(message)
                    raise
            else:
                print("Already downloaded", file_name)
            page_num += 1

    # Appends a '\' to the path name if none exists.
    def _add_end_slash(self, path):
        if path[-1] != '\\':
            path += '\\'
        return path

    def __str__(self):
        if (self.season_num == 1):
            return "%s Ch. %d" % (self.manga_name, self.chapter_num)
        return "%s S%d Ch. %d" % (self.manga_name, self.season_num, self.chapter_num)
