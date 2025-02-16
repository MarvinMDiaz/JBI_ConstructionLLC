import boto3
import smtplib


def get_ssm_parameter(name):
    """Fetch a parameter from AWS SSM Parameter Store"""
    ssm = boto3.client("ssm", region_name="us-east-1")  # Adjust to your AWS region
    response = ssm.get_parameter(Name=name, WithDecryption=True)
    return response["Parameter"]["Value"]

class Config:
    SECRET_KEY = get_ssm_parameter("/JBI/SECRET_KEY")
    RECAPTCHA_SITE_KEY = get_ssm_parameter("/JBI/RECAPTCHA_SITE_KEY")
    RECAPTCHA_SECRET_KEY = get_ssm_parameter("/JBI/RECAPTCHA_SECRET_KEY")
    RECIPIENT = get_ssm_parameter("/JBI/RECIPIENT")
    SES_USERNAME = get_ssm_parameter("/JBI/SES_USERNAME")
    SES_PASSWORD = get_ssm_parameter("/JBI/SES_PASSWORD")
    SES_SENDER = get_ssm_parameter("/JBI/SES_EMAIL_SENDER")
    MAIL_SERVER = 'email-smtp.us-east-1.amazonaws.com'  # Change to your SES SMTP endpoint
    MAIL_PORT = 587  # AWS SES supports 587 for TLS
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = get_ssm_parameter("/JBI/SES_SMTP_USERNAME")  # Your AWS SES SMTP username
    MAIL_PASSWORD= get_ssm_parameter("/JBI/SES_SMTP_PASSWORD")  # Your AWS SES SMTP password
