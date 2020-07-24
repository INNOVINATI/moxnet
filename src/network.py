from src.renderer import Renderer
from src.settings import Settings
from src.website import Website


class Network(object):

    def __init__(self, domains: list, settings: dict = None):
        self.sites = [Website(domain=d) for d in domains]
        self.settings = Settings(**settings)
        self.renderer = Renderer()

    def info(self):
        print('------ moxnet ------')
        print('Websites: ', len(self.sites))
        print('Pages: ', self.page_count)
        print('Links: ', self.link_count)
        print('--------------------')

    def build(self, path=None):
        for site in self.sites:
            site.build()
        self.renderer.render(self.sites, path)

    @property
    def page_count(self):
        return sum([len(s.pages) for s in self.sites])

    @property
    def link_count(self):
        return sum([len(p.links) for s in self.sites for p in s.pages.values()])

    def _link_sites(self):
        # TODO: Randomly inject links between websites by using Website.injext_links
        pass
