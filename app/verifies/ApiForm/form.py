#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.verifies.ApiForm.baseform import BaseForm
from wtforms import StringField
from wtforms.validators import DataRequired, length, ValidationError
from app.models.user import User


class RegisterForm(BaseForm):
    OpenID = StringField(validators=[DataRequired(message='不允许为空'), length(
        min=5, max=32
    )])
    session_key = StringField(DataRequired(message="不允许为空"))

    def validate_OpenID(self, form):
        user = User.query.filter_by(OpenID=form.data).first()
        if user:
            raise ValidationError(message='ID is exist')


class GetTokenForm(BaseForm):
    OpenID = StringField(validators=[DataRequired(message='不允许为空'), length(
        min=5, max=32
    )])
    session_key = StringField(DataRequired(message="不允许为空"))


class TokenForm(BaseForm):
    token = StringField(validators=[DataRequired()])
