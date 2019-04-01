#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint
from app.api.v1 import book, client, token, user, like


def create_blueprint():
    bpv1 = Blueprint('v1', __name__)
    book.api.register(bpv1)
    client.api.register(bpv1)
    token.api.register(bpv1)
    user.api.register(bpv1)
    like.api.register(bpv1)
    return bpv1
