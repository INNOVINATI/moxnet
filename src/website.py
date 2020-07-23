import random

import lorem as lorem


class Page(object):

    def __init__(self, id: int, domain: str):
        self.id = id
        self.domain = domain
        self.text = lorem.text()
        self.links = set([])

    def title(self):
        return f'{self.domain} - Page{self.id}'

    def url(self):
        return f'http://{self.domain}/page{self.id}.html'

    def build(self):
        # TODO: Convert links from integer to "/page{integer}.html" format
        pass


class Website(object):

    def __init__(self, domain, num_pages=10, ext_links=['http://google.com']):
        self.domain = domain
        self.external_links = ext_links
        prange = range(num_pages)
        self.pages = self._generate(len(prange))
        for link in self.external_links:
            # Insert external/real URLs at random
            page = random.choice(prange)
            self.pages[page].links.add(link)

    def _generate(self, size):
        ids = range(size)
        pages = {i: Page(id=i, domain=self.domain) for i in ids}
        reachable = {0}  # root page
        while len(reachable) < size:
            node = random.choice(list(reachable))
            k = random.randint(1, (len(ids)//3)+1)
            # Storing links as integers for simplicity and converting them to URL paths on render
            links = set(random.sample(ids, k=k))
            pages[node].links |= links
            reachable |= links
        return pages


