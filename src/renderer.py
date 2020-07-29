import os

from jinja2 import Environment, FileSystemLoader, select_autoescape

from website import Website


class Renderer(object):
    # TODO: Discuss how to handle exporting/building

    def __init__(self):
        self.engine = Environment(
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')), autoescape=select_autoescape(['html']))
        self.page_template = self.engine.get_template('page.html')
        self.nginx_template = self.engine.get_template('nginx.conf')

    def render(self, sites: [Website], path: str = None):
        sites_ = list(map(lambda site:
                        list(map(lambda page:
                                 self.page_template.render(page=page), site.pages)), sites))
        nginx_config = self.nginx_template.render(sites=sites)
        print(nginx_config)
        return sites_
