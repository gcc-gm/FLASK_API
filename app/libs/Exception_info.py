#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.libs.ApiErrors import APIException


class ClientException(APIException):
    code = 400
    message = " Validate Exception"
    error_code = 4000

    def __init__(self, message=None):
        if message:
            self.message = message
        super(ClientException, self).__init__(message=self.message,
                                              code=self.code,
                                              error_code=self.error_code)


class APISuccess(APIException):
    code = 201
    message = 'ok'
    error_code = 2001


class APIServerError(APIException):
    code = 500
    message = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 9000


class APINotFound(APIException):
    code = 404
    message = 'the resource are not found'
    error_code = 4004


class Forbidden(APIException):
    code = 403
    error_code = 4003
    message = 'api_forbidden'
