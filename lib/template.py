import os
import jinja2

# sets the home path to the templates folder
template_dir = os.path.join(os.path.dirname(__file__), '../templates')

# points jinja2 environment to the templates directory with XML/HMTL escape
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir),
    autoescape=True)

def render_env(template, **params):
    """ Gets the project templates and render with props to environment """
    t = jinja_env.get_template(template)
    return t.render(params)
