#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import current_app, g
from itsdangerous import TimedJSONWebSignatureSerializer \
    as Serializer, BadSignature, SignatureExpired

from app.libs.ApiErrors import APIException
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


class TokenOperation():
    @classmethod
    def generate_token(cls, **keyword):
        s = Serializer(current_app.config['SECRET_KEY'],
                       expires_in=current_app.config['EXPIRATION'])
        # 为byte, 故要编码
        return s.dumps(keyword).decode('utf-8')

    @classmethod
    def verify_token(cls, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except SignatureExpired:
            raise APIException(error_code=1003, message='token is timeout')
        except BadSignature:
            raise APIException(error_code=1002, message='token is bad')

        return data


@auth.verify_password
def verify_password(token, _):
    token = TokenOperation.verify_token(token)
    if token is None:
        return False
    else:
        g.uid = token
        return True


@auth.error_handler
def auth_error():
    raise APIException(error_code=1002, message='auth_error')
