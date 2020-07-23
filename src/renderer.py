from jinja2 import Environment, PackageLoader, select_autoescape

from src.network import Network


class Renderer(object):

    def __init__(self):
        self.engine = Environment(loader=PackageLoader('moxnet', 'templates'), autoescape=select_autoescape(['html']))
        self.template = self.engine.get_template('page.html')

    def render(self, network: Network):
        pass
