import os
import json

with open('/Users/austinbush/etc/config.json') as config_file:
    config = json.load(config_file)

class Config:
    SECRET_KEY = config['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = config['SQLALCHEMY_DATABASE_URI']
    MAIL_USERNAME = config['MAIL_USERNAME']
    MAIL_PASSWORD = config['MAIL_PASSWORD']
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True