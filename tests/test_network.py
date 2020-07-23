from unittest import TestCase

from src.network import Network


class TestNetworkInit(TestCase):
    def test_pages(self):
        domains = ['test1.local', 'test2.local']
        n = Network(domains=domains)
        self.assertEqual(n.page_count, 20)



