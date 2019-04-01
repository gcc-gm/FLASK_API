#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.models import db
from app.libs.ApiErrors import APIException
from app.libs.Exception_info import APISuccess
from app.libs.apiprint import ApiPrint
from app.models.user import User
from app.verifies.ApiForm.form import RegisterForm

api = ApiPrint('client')


@api.route('/register', methods=['POST'])
def create_client():
    form = RegisterForm()
    if form.api_validate():
        with db.auto_commit():
            user = User()
            user.session_key = form.session_key.data
            user.OpenID = form.OpenID.data
            db.session.add(user)
        return APISuccess()
    return APIException()
