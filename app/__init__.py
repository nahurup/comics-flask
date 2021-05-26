from flask import Flask, render_template
from .get_comics import get_list, get_pages
from .get_issues import get_issues


app=Flask(__name__)

@app.route('/<page>')
def index(page):
    data=get_list(page)
    return render_template('index.html', data=data, pages_number=get_pages(), page=page)

@app.route('/comic/<comic_name>')
def comic(comic_name):
    data=get_issues(comic_name)
    return render_template('comic.html', data=data, comic_name=comic_name)

def inicializarApp(config):
    app.config.from_object(config)
    return app