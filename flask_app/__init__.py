from flask import Flask
# import os
import smtplib


from flask_app.config import Config
app = Flask(__name__)
app.config.from_object(Config)

