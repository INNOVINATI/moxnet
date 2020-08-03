from unittest import TestCase

from src.generator import Generator
from src.website import Website


class TestGenerator(TestCase):
    def test_generator(self):
        g = Generator()
        w1 = Website('test1.local', num_pages=20)
        w2 = Website('test2.local', num_pages=20)
        g.generate(sites=[w1, w2], writeFile=False)
        self.assertEqual(len(g.sites), 2)
        self.assertEqual(len(g.sites[0]), 20)
        for i, html in enumerate(g.sites[0]):
            self.assertTrue(f'<title>{w1.domain} - Page{i}</title>' in html)
