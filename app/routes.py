from urllib.parse import unquote

from flask import request, render_template

from app import app, db
from app.models import ShortURL


@app.route('/')
def home():
    return 'Home'


@app.route('/add')
def add():
    """Create a short url via query string parameters."""
    url = unquote(request.args['url'])
    short = request.args['short']
    obj = ShortURL(
            url=url,
            short=short
        )
    db.session.add(obj)
    db.session.commit()
    return f"<strong>{obj.url}</strong> with <strong>{obj.short}</strong> successfully created!"


@app.route('/del')
def delete():
    """Delete a short url via query string parameters."""
    short = request.args['short']
    obj = ShortURL.query.filter_by(short=short).first_or_404()
    db.session.delete(obj)
    db.session.commit()
    return f"<strong>{short}</strong> successfully Deleted!"


@app.route('/data')
def data():
    res = {}
    for u in ShortURL.query.all():
        res[u.short] = u.url
    return res


@app.route('/<shortpath>')
def red(shortpath):
    obj = ShortURL.query.filter_by(short=shortpath).first_or_404()
    return render_template("redirect.html", redirect_url=obj.url)
