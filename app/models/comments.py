#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.models import db


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(256), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('users.id'))
    bid = db.Column(db.Integer, db.ForeignKey('boos.id'))

    @classmethod
    def to_json(cls):
        data = {
            'id': cls.id,
            'content': cls.content,
            'uid': cls.uid,
            'bid': cls.bid

        }
        return data
