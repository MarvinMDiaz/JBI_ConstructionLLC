from flask import Flask
import os
from flask_mail import Mail, Message
import smtplib
from config import Config
app = Flask(__name__)


app.config.from_object(Config)
mail = Mail(app)


app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config["MAIL_USERNAME"] = os.environ.get("EMAIL")
app.config["MAIL_PASSWORD"] = os.environ.get("EMAIL_PASSWORD")

mail = Mail(app)
