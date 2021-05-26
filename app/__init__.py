from flask import Flask, render_template
from .get_comics import get_list, get_pages


app=Flask(__name__)

@app.route('/<page>')
def index(page):
    data=get_list(page)
    return render_template('index.html', data=data, pages_number=get_pages(), page=page)


def inicializarApp(config):
    app.config.from_object(config)
    return app