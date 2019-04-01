#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_wtf import FlaskForm

from app.libs.Exception_info import ClientException


class BaseForm(FlaskForm):
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def api_validate(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # form errors
            raise ClientException(message=self.errors)
        return self
