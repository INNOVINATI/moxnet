from unittest import TestCase

from website import Website


class TestWebsiteInit(TestCase):
    def test_pages(self):
        w = Website('test.local', num_pages=42)
        self.assertEqual(len(w.pages), 42)

    def test_ext_links(self):
        links = ['https://duckduckgo.com', 'http://github.com']
        w = Website('test.local', ext_links=links)
        self.assertTrue(any([any([l in page.links for l in links]) for page in w.pages]))


