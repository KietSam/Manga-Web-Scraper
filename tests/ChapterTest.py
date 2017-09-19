import unittest
from Chapter import Chapter


class ChapterTest(unittest.TestCase):

    SECOND_SEASON_SINGLE_PAGE_URL = "http://mangaseeonline.us/read-online/The-Gamer-chapter-8-index-2-page-1.html"
    SECOND_SEASON_ALL_PAGES_URL = "http://mangaseeonline.us/read-online/The-Gamer-chapter-8-index-2.html"

    NO_SEASON_SINGLE_PAGE_URL = "http://mangaseeonline.us/read-online/The-Gamer-chapter-8-page-1.html"
    NO_SEASON_ALL_PAGES_URL = "http://mangaseeonline.us/read-online/The-Gamer-chapter-8.html"
    MESSED_UP_NO_SEASON_ALL_PAGES_URL = "http://mangaseeonline.us/read-onine/The-Gamer-chapter-8.html"

    def test_init_no_season_all_pages(self):
        chapter = Chapter(self.NO_SEASON_ALL_PAGES_URL)
        self.assertEqual(chapter.url, self.NO_SEASON_ALL_PAGES_URL)
        self.assertEqual(chapter.chapter_num, 8)
        self.assertEqual(chapter.season_num, 1)
        self.assertEqual(chapter.manga_name, "The Gamer")

    def test_init_no_season_single_page(self):
        chapter = Chapter(self.NO_SEASON_SINGLE_PAGE_URL)
        self.assertEqual(chapter.url, self.NO_SEASON_ALL_PAGES_URL)
        self.assertEqual(chapter.chapter_num, 8)
        self.assertEqual(chapter.season_num, 1)
        self.assertEqual(chapter.manga_name, "The Gamer")

    def test_init_messed_up_no_season_single_page(self):
        with self.assertRaises(Exception) as ex:
            Chapter(self.MESSED_UP_NO_SEASON_ALL_PAGES_URL)
        self.assertEqual(str(ex.exception), "Wrong starting url detected: http://mangaseeonline.us/read-onine/T")

    def test_init_second_season_all_pages(self):
        chapter = Chapter(self.SECOND_SEASON_ALL_PAGES_URL)
        self.assertEqual(chapter.url, self.SECOND_SEASON_ALL_PAGES_URL)
        self.assertEqual(chapter.chapter_num, 8)
        self.assertEqual(chapter.season_num, 2)
        self.assertEqual(chapter.manga_name, "The Gamer")

    def test_init_second_season_single_page(self):
        chapter = Chapter(self.SECOND_SEASON_SINGLE_PAGE_URL)
        self.assertEqual(chapter.url, self.SECOND_SEASON_ALL_PAGES_URL)
        self.assertEqual(chapter.chapter_num, 8)
        self.assertEqual(chapter.season_num, 2)
        self.assertEqual(chapter.manga_name, "The Gamer")

if __name__ == "__main__":
    unittest.main()