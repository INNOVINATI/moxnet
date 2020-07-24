import os

from jinja2 import Environment, FileSystemLoader, select_autoescape

from src.website import Website


class Renderer(object):
    # TODO: Discuss how to handle exporting/building

    def __init__(self):
        self.engine = Environment(
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')), autoescape=select_autoescape(['html']))
        self.template = self.engine.get_template('page.html')

    def render(self, sites: [Website], path: str = None):
        pass
