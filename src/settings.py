class Settings(object):

    def __init__(self, domains: int = 5, pages: int = 50, link_sites: bool = False):
        self.domains = domains
        self.pages = pages
        self.interlink = link_sites
