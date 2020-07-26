class Settings(object):
    def __init__(self, num_domains: int = 1, num_pages: int = 1, num_externals: int = 1, link_sites: bool = False):
        if not isinstance(num_pages / num_domains, int):
            raise Exception(
                'Given number of pages is not divisible by the number of domains: ', num_pages, num_domains)
        self.num_domains = num_domains
        self.num_pages = num_pages
        self.num_externals = num_externals
        self.interlink = link_sites
