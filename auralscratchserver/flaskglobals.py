from pathlib import Path

from flask import Flask

from .db.api import AuralScratchDB
from .db.fsimpl import FileSystemDB
from .flaskext import extensions

app = Flask(__package__, root_path='.')

for e in extensions:
    e.extend(app)

db: AuralScratchDB = FileSystemDB(Path('./db'))
