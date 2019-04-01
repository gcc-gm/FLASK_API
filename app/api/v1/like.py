#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, g

from app.libs.Token import auth
from app.libs.apiprint import ApiPrint
from app.models.book import Book

api = ApiPrint('like')


@api.route('/<int:bid>', methods=['POST'])
@auth.login_required
def like(bid):
    book = Book.query.get_or_404(bid)
    uid = g.uid['uid']
    print(uid,bid)
    return '12'


@api.route('/cancel/<int:bid>', methods=['POST'])
@auth.login_required
def cancel(bid):
    book = Book.query.get_or_404(bid)
    return 'dfasfas'
