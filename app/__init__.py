from flask import Flask, render_template
from .get_comics import get_list


app=Flask(__name__)

@app.route('/')
def index():
    data=get_list(1)
    return render_template('index.html', data=data)


def inicializarApp(config):
    app.config.from_object(config)
    return app