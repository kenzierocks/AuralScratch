from flask import render_template, request

from .flaskglobals import app, db


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/songs')
def songs():
    return render_template('songs.html', songs=db.songs.get_map().values())


@app.route('/tags')
def tags():
    return render_template('tags.html', tags=db.tags.get_map().values())


@app.route('/tag-categories')
def tag_categories():
    return render_template('tag-categories.html', tag_categories=db.tag_categories.get_map().values())


@app.route('/playlists')
def playlists():
    return render_template('playlists.html', playlists=db.playlists.get_map().values())


@app.route('/<path:template>')
def any_template(template):
    return render_template(template + '.html')
