#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.ApiErrors import APIException
from app.models.base import _Base
from app.models import db


class User(_Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    OpenID = db.Column(db.String(5), unique=True, nullable=False)
    _session_key = db.Column('session_key', db.String(128), nullable=False)
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def session_key(self):
        return self._session_key

    @session_key.setter
    def session_key(self, key):
        self._session_key = generate_password_hash(key)

    @staticmethod
    def user_verify(id, key):
        user = User.query.filter_by(OpenID=id).first()
        if not user:
            raise APIException(code=404, error_code=2000, message='no this user')
        if not user.check_key(key):
            raise APIException(code=401, error_code=4001, message='Authorization fail')
        return {'uid': user.id}

    # 利用此函数来实现验证， 返回的是True, False
    def check_key(self, key):
        return check_password_hash(self._session_key, key)
