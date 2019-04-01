#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import current_app, url_for
from flask.json import jsonify

from app.models import db
from app.models.base import _Base


class Book(_Base):
    __tablename__ = 'books'
    """
        一些属性定义重复性比较大，元类可以解决这个问题
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=True)
    author = db.Column(db.String(20), default='未名')
    publisher = db.Column(db.String(15))
    price = db.Column(db.Integer)
    summary = db.Column(db.String(500), default='无')
    _image = db.Column('image', db.String(20))
    comments = db.relationship('Comment', backref='book', lazy='dynamic')

    @property
    def image(self):
        from flask import url_for
        burl = url_for('static', filename='book/image/', _external=True) + self._image
        return burl

    @image.setter
    def image(self, value):
        self._image = value

    @classmethod
    def get_books(cls, page):
        next, prev = None, None
        pagination = Book.query.order_by(
            Book.create_time).paginate(
            page=page, per_page=current_app.config['BOOK_LIMIT'],
            error_out=False)

        # items取得recent_books的模型列表
        books = pagination.items

        if pagination.has_next:
            next = url_for('v1.recent', page=page + 1, _external=True)
        if pagination.has_prev:
            prev = url_for('v1.recent', page=page + 1, _external=True)
        data = jsonify({
            'books': [ book.to_json() for book in books ],
            'prev': prev,
            'next': next,
            'count': pagination.total
        })
        return data

    def to_json(self):
        json_book = {
            'url': url_for('v1.recent', bid=self.id, _external=True),
            'title': self.title,
            'author': self.author,
            'publisher': self.publisher,
            'price': self.price,
            'summary': self.summary,
            'image': self.image
        }
        return json_book
