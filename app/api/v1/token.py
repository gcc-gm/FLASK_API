#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.json import jsonify

from app.libs.Token import TokenOperation
from app.libs.apiprint import ApiPrint
from app.models.user import User
from app.verifies.ApiForm.form import GetTokenForm

api = ApiPrint('token')


@api.route('', methods=['POST'])
def get_token():
    form = GetTokenForm().api_validate()
    uid = User.user_verify(id=form.OpenID.data, key=form.session_key.data)
    token = TokenOperation.generate_token(**uid)
    return jsonify({'token': token}), 201
