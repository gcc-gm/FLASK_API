#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contextlib import contextmanager
from flask_sqlalchemy import BaseQuery, SQLAlchemy as sql

from app.libs.ApiErrors import APIException
from app.libs.Exception_info import APINotFound


class SQLAlchemy(sql):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            type(e)
            raise APIException(error_code=4001, message=e.args)


class Query(BaseQuery):

    def get_or_404(self, id):

        rv = self.get(id)
        if rv is None or rv.status == 0:
            raise APINotFound(message='get_or_404 error')
        return rv

    def first_or_404(self):

        rv = self.first()
        if rv is None or rv.status == 0:
            raise APINotFound(message='first_or_404 error')
        return rv


db = SQLAlchemy(query_class=Query)
