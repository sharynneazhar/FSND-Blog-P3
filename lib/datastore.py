from google.appengine.ext import db
from template import render_env
from hashstore import *

def users_key(group = 'default'):
    return db.Key.from_path('users', group)

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class User(db.Model):
    """ Creates an entity to store user data in the GAE datastore """
    name = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True)
    email = db.StringProperty()

    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(uid, parent = users_key())

    @classmethod
    def by_name(cls, name):
        u = User.all().filter('name =', name).get()
        return u

    @classmethod
    def register(cls, name, pw, email = None):
        pw_hash = make_pw_hash(name, pw)
        return User(parent = users_key(),
                    name = name,
                    pw_hash = pw_hash,
                    email = email)

    @classmethod
    def login(cls, name, pw):
        u = cls.by_name(name)
        if u and valid_pw(name, pw, u.pw_hash):
            return u

class Post(db.Model):
    """ Creates an entity to store blog post data in the GAE datastore """
    author = db.StringProperty()
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateProperty(auto_now_add = True)
    modified = db.DateTimeProperty(auto_now = True)
    votes = db.IntegerProperty(default=0)
    upvoters = db.StringListProperty()
    downvoters = db.StringListProperty()

    def render(self):
        """
        Renders blog post to environment
        _render_text replaces return characters with HTML breaks so that
        it renders properly in the browser
        """
        self._render_text = self.content.replace('\n', '<br>')
        return render_env("post.html", p=self)

class Comment(db.Model):
    """ Creates an entity to store comments in the GAE datastore """
    author = db.StringProperty()
    post_id = db.StringProperty(required = True)
    comment = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now = True)
