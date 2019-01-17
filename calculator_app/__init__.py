from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('home', '/calculator')
    config.add_route('add', '/calculator/add')
    config.add_route('substract', '/calculator/substract')
    config.add_route('multiply', '/calculator/multiply')
    config.add_route('divide', '/calculator/divide')
    config.scan('.views')
    return config.make_wsgi_app()