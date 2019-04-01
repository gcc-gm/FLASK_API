#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from app.api.v1 import create_blueprint
from app.models import db


def sql_init(app):
    db.init_app(app)
    # db.drop_all(app=app)
    db.create_all(app=app)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secrecy')

    sql_init(app)

    app.register_blueprint(create_blueprint(), url_prefix='/v1')

    return app
