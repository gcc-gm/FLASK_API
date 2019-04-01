#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SingleBook():
    def __init__(self, book):
        self.id = book.id
        self.title = book.title
        self.author = book.author
        self.publisher = book.publisher
        self.price = book.price
        self.summary = book.summary
        self.image = book.image


class SeveralBooks():
    def __init__(self):
        self.total = 0
        self.books = []

    def filter(self, books):
        self.total = len(books)
        self.books = [SingleBook(book) for book in books]
