import random

import lorem as lorem


class Page(object):

    def __init__(self, id: int, subdomain: str):
        self.id = id
        self.subdomain = subdomain
        self.text = lorem.text()
        self.links = set([])
        self.path = self.format_url(self.id)
        self.html = None

    @property
    def domain(self):
        return f'{self.subdomain}.moxnet.local'

    @property
    def title(self):
        return f'{self.domain} - Page{self.id}'

    def format_url(self, id):
        return f'http://{self.domain}/page{id}.html'

    def build(self):
        self.links = [self.format_url(link) if isinstance(link, int) else link for link in self.links]


class Website(object):

    def __init__(self, subdomain: str, num_pages=10, ext_links=['http://google.com', 'http://www.example.com']):
        self.subdomain = subdomain
        self.external_links = ext_links
        self.pages = self._generate(num_pages)
        self.build()

    @property
    def domain(self):
        return f'{self.subdomain}.moxnet.local'

    def injext_links(self, links: [int] = None):
        ls = links if links else self.external_links
        for link in ls:
            # Insert external/real URLs at random
            page = random.choice(self.pages)
            self.pages[page.id].links.add(link)

    def _generate(self, size):
        ids = range(int(size))
        pages = [Page(id=i, subdomain=self.subdomain) for i in ids]
        reachable = {0}  # root page
        while len(reachable) < size:
            node = random.choice(list(reachable))
            k = random.randint(1, (len(ids)//3)+1)
            # Storing links as integers for simplicity and converting them to URL paths on generate
            links = set(random.sample(ids, k=k))
            pages[node].links |= links
            reachable |= links
        return pages

    def build(self):
        self.injext_links()
        for page in self.pages:
            page.build()

