#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request

from app.libs.apiprint import ApiPrint
from app.models.book import Book

api = ApiPrint('comment')


@api.route('', methods=['GET'])
def get_comments():
    bid = request.args.get('bid',type=int)
    book = Book.query.get_or_404(bid)

