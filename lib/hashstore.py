import random
import hashlib
import hmac

from string import letters

SECRET_COOKIE = 'TKLTerO42XkHJ8c'

def make_salt(length = 5):
    """ Generates a salt to pair with hash keys """
    return ''.join(random.choice(letters) for x in xrange(length))

def make_pw_hash(name, pw, salt = None):
    """ Salt password if none exist, otherwise create hash """
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (salt, h)

def make_secure_val(val):
    """ Pairs the cookie with secret string """
    return '%s|%s' % (val, hmac.new(SECRET_COOKIE, val).hexdigest())

def check_secure_val(secure_val):
    """ Make sure the cookie is valid """
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val

def valid_pw(name, password, h):
    """ Checks if a password is valid """
    salt = h.split(',')[0]
    return h == make_pw_hash(name, password, salt)
