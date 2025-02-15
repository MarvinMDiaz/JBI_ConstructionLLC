from flask import Flask
import os
import smtplib
from flask_app.config import Config
app = Flask(__name__)


app.config.from_object(Config)

app.config['MAIL_SERVER'] = 'email-smtp.us-east-1.amazonaws.com'  # Change to your SES SMTP endpoint
app.config['MAIL_PORT'] = 587  # AWS SES supports 587 for TLS
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get("SES_SMTP_USERNAME")  # Your AWS SES SMTP username
app.config['MAIL_PASSWORD'] = os.environ.get("SES_SMTP_PASSWORD")  # Your AWS SES SMTP password
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get("SES_EMAIL_SENDER")  # Your verified email

