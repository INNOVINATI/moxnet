import os
<<<<<<< HEAD

from jinja2 import Environment, PackageLoader, select_autoescape

=======

from jinja2 import Environment, FileSystemLoader, select_autoescape

>>>>>>> dbb5199430e6182837f367895a073a0ac883ddab
from src.website import Website


class Renderer(object):
    # TODO: Discuss how to handle exporting/building

    def __init__(self):
        self.engine = Environment(
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')), autoescape=select_autoescape(['html']))
        self.template = self.engine.get_template('page.html')

    def render(self, sites: [Website], path: str = None):
<<<<<<< HEAD
        pass
=======
        return list(map(lambda site:
                        list(map(lambda page:
                                 self.template.render(page=page), site.pages)), sites))
>>>>>>> dbb5199430e6182837f367895a073a0ac883ddab
