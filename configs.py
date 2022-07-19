from datetime import timedelta
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
JSON_AS_ASCII = False ##編碼不使用ASCII
DEBUG = True
SECRET_KEY = b'\x00I<\xa4Vn1\xf7\xc5\xfb\xed\xcc"+\xce\xdc'
PERMANENT_SESSION_LIFETIME = timedelta(days=31)
SESSION_USE_SIGNER = True
SESSION_COOKIE_NAME = "session"