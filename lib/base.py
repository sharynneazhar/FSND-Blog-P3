import webapp2

from lib.regex import *
from lib.template import *
from lib.datastore import *

class BaseHandler(webapp2.RequestHandler):
    """ Base handler for all classes """
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_tmpl(self, template, **params):
        """ Passes the template and its parameters to jinja environment """
        params['user'] = self.user
        return render_env(template, **params)

    def render(self, template, **kw):
        """ Calls render_templ and render the jinja environment """
        self.write(self.render_tmpl(template, **kw))

    def set_secure_cookie(self, name, val):
        """ Creates a cookie based on a given name and value """
        cookie_val = make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))

    def read_secure_cookie(self, cookie):
        """ Returns the value of the cookie itself """
        cookie_val = self.request.cookies.get(cookie)
        return cookie_val and check_secure_val(cookie_val)

    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))

    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        self.user = uid and User.by_id(int(uid))
