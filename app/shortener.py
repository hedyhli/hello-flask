from ast import literal_eval as to_int
from secrets import SystemRandom

from short_url import encode_url

from app.models import ShortURL


randint = SystemRandom().randint

def shorten(url: str):
    dec = to_int('0x' + bytes(url, 'utf-8').hex())
    res = encode_url(dec)[:8]

    while ShortURL.query.filter_by(short=res).first():
        res = shorten(res + randint(0, 100))
    return res