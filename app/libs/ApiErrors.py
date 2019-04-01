#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, json
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    message = 'unknown errors'
    error_code = 1000

    def __init__(self, message=None, code=None, error_code=None,
                 headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if message:
            self.message = message
        super(APIException, self).__init__(message, response=None)

    def get_body(self, environ=None):
        body = dict(
            message=self.message,
            error_code=self.error_code,
            request_method=request.method,
            request_url=request.url
        )
        content = json.dumps(body)
        return content

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]
