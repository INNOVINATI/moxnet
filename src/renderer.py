import os

from jinja2 import Environment, PackageLoader, select_autoescape

from src.website import Website


class Renderer(object):
    # TODO: Discuss how to handle exporting/building
    folder = os.path.join(os.getcwd(), 'html')

    def __init__(self):
        self.engine = Environment(loader=PackageLoader('moxnet', 'templates'), autoescape=select_autoescape(['html']))
        self.template = self.engine.get_template('page.html')

    def render(self, sites: [Website]):
        pass
