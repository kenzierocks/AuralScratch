import sys
from pathlib import PurePath

from flask import url_for, Flask
from werkzeug.routing import BuildError

from .ext import FlaskExtension

STATIC_FILE_MIXINS = ('css', 'js', 'img')


class StaticFileMixinsExtension(FlaskExtension):
    def extend(self, app: Flask):
        def fail_handler(error, exc_info):
            # External lookup did not have a URL.
            # Re-raise the BuildError, in context of original traceback.
            exc_type, exc_value, tb = exc_info
            if exc_value is error:
                raise exc_type(exc_value).with_traceback(tb)
            else:
                raise error

        def _get_extension(endpoint, values):
            if endpoint in ('css', 'js'):
                return endpoint
            if endpoint in ('img',):
                return values['type']

                # Map CSS/JS/IMG to static files

        def static_css_and_js(error, endpoint, values):
            exc_info = sys.exc_info()
            if endpoint not in STATIC_FILE_MIXINS:
                fail_handler(error, exc_info)
                return
            try:
                values_copy = dict(values)
                values_copy['filename'] = str(
                    PurePath(endpoint) / (values_copy['name'] + '.' + _get_extension(endpoint, values)))
                del values_copy['name']
                return url_for('static', **values_copy)
            except BuildError:
                fail_handler(error, exc_info)
                raise

        app.url_build_error_handlers.append(static_css_and_js)
