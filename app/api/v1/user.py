#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request

from app.libs.Token import auth
from app.libs.apiprint import ApiPrint
from app.models.user import User

api = ApiPrint('user')


@api.route('/', methods=['GET'])
@auth.login_required
def get_user():
    uid = request.args.get('uid',121,type=int)

    # user = User.query.get_or_404(uid)
    # return user.id
    return uid


