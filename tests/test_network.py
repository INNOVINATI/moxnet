from unittest import TestCase

from src.network import Network
from src.settings import Settings

class TestNetworkInit(TestCase):
    def test_pages(self):
        s = Settings(num_domains=2, num_pages=20)
        n = Network(s)
        self.assertEqual(n.page_count, 20)



