from Manga import Manga
from Chapter import Chapter

SAVE_PATH = "D:\Downloads\Test"

manga_url = "http://mangaseeonline.us/manga/Mirai-Nikki-Paradox"

chapter_url = "http://mangaseeonline.us/read-online/One-Piece-chapter-878-page-1.html"

chapter_url_with_seasons = "http://mangaseeonline.us/read-online/The-Gamer-chapter-8-index-2-page-1.html"

# chapter_test = Chapter(chapter_url_with_seasons)
#
# print(chapter_test.url)

# chapter_test.download_chapter(SAVE_PATH)

# for chapter in manga_test.chapters:
#     print("Chapter %d" % chapter.chapter_num)
#     print(chapter.image_urls)


def run():
    manga_test = Manga("http://mangaseeonline.us/manga/Haikyu")
    manga_test.parallel_download_manga(SAVE_PATH)


if __name__ == '__main__':
    run()
