"""Insta485 development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'I\xfd)\x9a\xfe\xac\xd4\x08\
    xae0\xb8\x9d\x03kJ\xf2\x90\x1a\x99TM\x96\x00I'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
FINFO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DATABASE_FILENAME = FINFO_ROOT/'var'/'finfo.sqlite3'