from .flaskglobals import app

from importlib import import_module

import_module('.routing', __package__)
