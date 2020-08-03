import errno
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape

from src.website import Website


class Generator(object):
    sites = dict()

    def __init__(self):
        self.engine = Environment(
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
            autoescape=select_autoescape(['html'])
        )
        self.page_template = self.engine.get_template('page.html')
        self.server_template = self.engine.get_template('nginx.conf')

    def generate(self, sites: [Website], path: str = None, writeFile: bool = False):
        export_to = path if path else os.path.join(os.getcwd(), 'moxnet')
        self.sites = list(map(lambda site: list(map(lambda page: self.page_template.render(page=page), site.pages)), sites))
        page_template = self.engine.get_template('page.html')
        server_template = self.server_template.render(sites=sites)  #TODO: Implement file writing

        if not writeFile:
            return

        for site in sites:
            dir = os.path.join(export_to, site.domain)
            os.makedirs(dir, exist_ok=True)
            for page in site.pages:
                p = page_template.render(page=page)
                filepath = os.path.join(dir, f'page{page.id}.html')
                with open(filepath, "w") as f:
                    f.write(p)
