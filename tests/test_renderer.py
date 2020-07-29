from unittest import TestCase

from renderer import Renderer
from website import Website


class TestRendererInit(TestCase):
    def test_renderer(self):
        r = Renderer()
        w = Website('test.local', num_pages=2)
        rendered_sites = r.render(sites=[w])
        self.assertEqual(len(rendered_sites), 1)
        self.assertEqual(len(rendered_sites[0]), 2)
        for i, html in enumerate(rendered_sites[0]):
            self.assertTrue(f'<title>test.local - Page{i}</title>' in html)
