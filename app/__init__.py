from flask import Flask, render_template
from .get_comics import get_list, get_pagination_max
from .get_issues import get_issues
from .get_info import get_info
from .get_pages import get_pages


app=Flask(__name__)

@app.route('/<page>')
def index(page):
    data=get_list(page)
    return render_template('index.html', data=data, pages_number=get_pagination_max(), page=page)

@app.route('/comic/<comic_name>')
def comic(comic_name):
    data=get_issues(comic_name)
    comic_info=get_info(comic_name)
    return render_template('comic.html', data=data, comic_name=comic_name, comic_info=comic_info)

@app.route('/comic/<comic_name>/<issue_number>')
def issue(comic_name, issue_number):
    issue=get_pages(comic_name, issue_number)
    comic_info=get_info(comic_name)
    return render_template('issue.html', issue=issue, issue_number=issue_number, comic_info=comic_info)

def inicializarApp(config):
    app.config.from_object(config)
    return app