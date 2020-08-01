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

    def generate(self, sites: [Website], path: str = None):
        export_to = path if path else os.path.join(os.getcwd(), 'moxnet')
        self.sites = list(map(lambda site: list(map(lambda page: self.page_template.render(page=page), site.pages)), sites))
        page_template = self.engine.get_template('page.html')
        server_template = self.server_template.render(sites=sites)  #TODO: Implement file writing
        for site in sites:
            for page in site.pages:
                p = page_template.render(page=page)
                #TODO: Pull the check outside of the loops
                f = os.path.join(export_to, site.domain, f'page{page.id}.html')
                if not os.path.exists(os.path.dirname(f)):
                    try:
                        os.makedirs(os.path.dirname(f))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                with open(f, "w") as f:
                    f.write(p)
