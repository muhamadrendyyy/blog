#import aplikasi flask untuk dipakai di web kita
import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='def',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

def create_app():
    app = ...

    from . import db
    db.init_app(app)

    return app

def create_app():
    app = ...

    from . import auth
    app.register_blueprint(auth.bp)

    return app

def create_app():
    app = ...
    #existing code omitted

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')