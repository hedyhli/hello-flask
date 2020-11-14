from app import app, db
from app.models import ShortURL
from app.shortener import shorten


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'ShortURL': ShortURL, 'shorten': shorten}
