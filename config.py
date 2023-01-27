import os


class Config:

    SECRET_KEY = os.environ.get("SECRET_KEY")
    EMAIL = os.environ.get("EMAIL")
    EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
