from flask import Flask
from .blueprints.site.routes import site

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

app.register_blueprint(site)