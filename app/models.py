from app import db

class ShortURL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(), index=True, unique=True)
    short = db.Column(db.String(8), index=True, unique=True)

    def __repr__(self):
        return '<ShortURL {}>'.format(self.url)    