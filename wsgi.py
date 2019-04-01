#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.ApiErrors import APIException

app = create_app()


@app.route('/',methods=['GET'])
def index():
    return 'index'


@app.errorhandler(Exception)
def flask_errors(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        error_code = 5000
        code = e.code
        message = e.description
        return APIException(error_code=error_code, code=code, message=message)
    else:
        raise e
        # return APIException()
        # 调试模式
        # log
        # if not app.config['DEBUG']:
        #     return APIException()
        # else:
        #     raise e
        # raise e


if __name__ == '__main__':
    app.run()
