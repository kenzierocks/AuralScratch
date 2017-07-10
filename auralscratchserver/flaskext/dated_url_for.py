from flask import url_for, Flask
import os

from .ext import FlaskExtension


class DatedUrlForExtension(FlaskExtension):
    def extend(self, app: Flask):
        @app.context_processor
        def override_url_for():
            """
            Overrides url_for in templates to add the modified time of the file.
            This breaks the caches when the files are updated.
            """
            return dict(url_for=dated_url_for)

        def dated_url_for(endpoint, **values):
            if endpoint == 'static':
                filename = values.get('filename', None)
                if filename:
                    file_path = os.path.join(app.root_path,
                                             endpoint, filename)
                    values['cacheTime'] = int(os.stat(file_path).st_mtime)
            return url_for(endpoint, **values)
