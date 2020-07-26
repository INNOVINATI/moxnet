import random

import lorem as lorem


class Page(object):

    def __init__(self, id: int, domain: str):
        self.id = id
        self.domain = domain
        self.text = lorem.text()
        self.links = set([])
        self.path = self.format_url(self.id)

    @property
    def title(self):
        return f'{self.domain} - Page{self.id}'

    def format_url(self, id):
<<<<<<< HEAD
        return f'http://{self.domain}/page{id}.html'
=======
        url = f'http://{self.domain}.moxnet.local'
        if id == 0:
            return f'{url}/index.html'
        return f'{url}/page{id}.html'
>>>>>>> dbb5199430e6182837f367895a073a0ac883ddab

    def build(self):
        self.links = [self.format_url(link) if type(link) is int else link for link in self.links]


class Website(object):

    def __init__(self, domain: str, num_pages=10, ext_links=['http://google.com', 'http://www.example.com']):
        self.domain = domain
        self.external_links = ext_links
        self.pages = self._generate(num_pages)
        self.injext_links()

    def injext_links(self, links: [int] = None):
        ls = links if links else self.external_links
        for link in ls:
            # Insert external/real URLs at random
<<<<<<< HEAD
            page = random.choice(len(self.pages))
            self.pages[page].links.add(link)
=======
            page = random.choice(self.pages)
            self.pages[page.id].links.add(link)
>>>>>>> dbb5199430e6182837f367895a073a0ac883ddab

    def _generate(self, size: int):
        ids = range(size)
        pages = [Page(id=i, domain=self.domain) for i in ids]
        reachable = {0}  # root page
        while len(reachable) < size:
            node = random.choice(list(reachable))
            k = random.randint(1, (len(ids)//3)+1)
            # Storing links as integers for simplicity and converting them to URL paths on render
            links = set(random.sample(ids, k=k))
            pages[node].links |= links
            reachable |= links
        return pages

    def build(self):
        for page in self.pages:
            page.build()

