#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask.json import jsonify

from app.libs.apiprint import ApiPrint
from app.models.book import Book

api = ApiPrint('book')


@api.route('/recent', methods=['GET'])
def recent():
    page = request.args.get('page', 1, type=int)
    books = Book.get_books(page)
    return books


@api.route('/', methods=['GET'])
def book_info():
    bid = request.args.get('bid', type=int)
    book = Book.query.get_or_404(bid)
    data = book.to_json()
    return jsonify(data)
