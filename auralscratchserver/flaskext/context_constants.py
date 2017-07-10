from flask import Flask
from .ext import FlaskExtension


class NavbarLink:
    def __init__(self, name: str, endpoint: str):
        self.name = name
        self.endpoint = endpoint


def _nl(name: str, endpoint: str) -> NavbarLink:
    return NavbarLink(name, endpoint)


class ContextConstantsExtension(FlaskExtension):
    def extend(self, app: Flask):
        @app.context_processor
        def add_constants():
            return {
                'navbar_links': [
                    _nl('Home', 'index'),
                    _nl('Songs', 'songs'),
                    _nl('Tags', 'tags'),
                    _nl('Tag Categories', 'tag_categories'),
                    _nl('Playlists', 'playlists')
                ]
            }
