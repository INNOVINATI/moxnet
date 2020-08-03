from unittest import TestCase

from src.generator import Generator
from src.website import Website


class TestGenerator(TestCase):
    def test_generator(self):
        g = Generator()
        w1 = Website('test1', num_pages=20)
        w2 = Website('test2', num_pages=20)
        g.generate(sites=[w1, w2], writeFile=True)
        self.assertEqual(len(g.sites), 2)
        self.assertEqual(len(g.sites[0].pages), 20)
        for i, page in enumerate(g.sites[0].pages):
            self.assertTrue(f'<title>{w1.domain} - Page{i}</title>' in page.html)
