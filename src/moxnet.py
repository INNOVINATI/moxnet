import click

from network import Network
from settings import Settings


@click.command()
@click.option('--num_domains', default=1, help='Number of domains.')
@click.option('--num_pages', default=1, help='Total number of pages.')
@click.option('--num_externals', default=1, help='Number of external domains.')
@click.option('--link_sites', default=False, help='Interlink.')
def moxnet(**settings):
    settings = Settings(**settings)
    n = Network(settings)
    n.info()


if __name__ == "__main__":
    moxnet()
