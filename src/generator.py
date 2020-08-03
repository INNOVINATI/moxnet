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
        self.sites = sites
        self.config = self.server_template.render(sites=sites)

        for site in sites:
            for page in site.pages:
                page.html = self.page_template.render(page=page)

        if not writeFile:
            return

        dir_root = path if path and os.path.isdir(path) else os.path.join(os.getcwd(), 'moxnet')
        os.makedirs(dir_root, exist_ok=True)

        for site in sites:
            dir = os.path.join(dir_root, site.domain)
            os.makedirs(dir, exist_ok=True)
            for page in site.pages:
                filepath = os.path.join(dir, f'page{page.id}.html')
                with open(filepath, "w") as f:
                    f.write(page.html)

        filepath = os.path.join(dir_root, f'nginx.conf')
        with open(filepath, "w") as f:
            f.write(self.config)
