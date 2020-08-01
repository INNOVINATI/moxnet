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
        self.template = self.engine.get_template('page.html')

    def generate(self, sites: [Website], path: str = None):
        export_to = path if path else os.path.join(os.getcwd(), 'moxnet')
        self.sites = list(map(lambda site: list(map(lambda page: self.template.render(page=page), site.pages)), sites))
        template = self.engine.get_template('page.html')
        for site in sites:
            for page in site.pages:
                p = template.render(page=page)
                f = os.path.join(export_to, site.domain, f'page{page.id}.html')
                if not os.path.exists(os.path.dirname(f)):
                    try:
                        os.makedirs(os.path.dirname(f))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                with open(f, "w") as f:
                    f.write(p)

