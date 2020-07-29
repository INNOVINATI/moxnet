import random

from src.renderer import Renderer
from src.settings import Settings
from src.website import Website


class Network(object):

    def __init__(self, settings: Settings):
        self.settings = settings
        self.sites = []
        num_pages = settings.num_pages//settings.num_domains
        for i in range(settings.num_domains):
            domain = f'site{i}'
            k = random.randint(0, settings.num_externals)
            ext_links = random.sample(range(settings.num_externals), k)
            w = Website(domain=domain, num_pages=num_pages, ext_links=ext_links)
            self.sites.append(w)
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
        return sum([len(p.links) for s in self.sites for p in s.pages])

    def _link_sites(self):
        # TODO: Randomly inject links between websites by using Website.injext_links
        pass
