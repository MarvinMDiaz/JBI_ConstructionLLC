from flask import render_template, request, redirect, session, Flask
import boto3  
from config import Config 
import requests
from flask_app import app
from flask import flash
import os
from flask_app.models.formValidation import User
from flask_mail import Mail, Message
from datetime import datetime
import logging
from flask_wtf.csrf import CSRFProtect

mail = Mail(app)
csrf = CSRFProtect(app)

RECAPTCHA_SECRET_KEY = Config.RECAPTCHA_SECRET_KEY


@app.route('/')
def homepage():
    current_year = datetime.now().year
    return render_template('Home.html', current_year=current_year,recaptcha_site_key=app.config['RECAPTCHA_SITE_KEY'])



@app.route('/submitted', methods=["POST"])
def contactForm():
    try:
        # Get reCAPTCHA response from the form
        recaptcha_response = request.form.get('g-recaptcha-response')
        verification_url = 'https://www.google.com/recaptcha/api/siteverify'
        payload = {
            'secret': Config.RECAPTCHA_SECRET_KEY,  # Now using SSM value
            'response': recaptcha_response
        }
        response = requests.post(verification_url, data=payload)
        result = response.json()

        if not result.get('success'):
            flash("reCAPTCHA verification failed. Please try again.", 'recaptcha')
            logging.error(f"reCAPTCHA failed: {result}")
            return redirect("/#Contact")

        # Validate form inputs
        if not User.validate_form(request.form):
            logging.warning("Form validation failed.")
            return redirect("/#Contact")

        # Process form details
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Replace Flask-Mail with SES
        ses_client = boto3.client("ses", region_name="us-east-1")
        response = ses_client.send_email(
            Source=Config.SES_SENDER,  # Sender email from SSM
            Destination={"ToAddresses": [Config.RECIPIENT]},  # Recipient from SSM
            Message={
                "Subject": {"Data": f"New Website Contact Form: {name}"},
                "Body": {
                    "Text": {"Data": f"""
                    Client's Name: {name}
                    Email: {email}
                    Phone Number: {phone}
                    Message: {message}
                    """}
                },
            },
        )

        flash(f"Thank you, {name}! Your message was successfully sent.", "success")
        logging.info(f"Form successfully submitted by {name}.")

    except requests.exceptions.RequestException as e:
        logging.error(f"Error while verifying reCAPTCHA: {e}")
        flash("An error occurred while verifying reCAPTCHA. Please try again later.", "recaptcha")
        return redirect("/#Contact")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        flash("An unexpected error occurred. Please try again later.", "error")
        return redirect("/#Contact")

    return redirect("/success")

@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/sitemap.xml')
def sitemap():
    return render_template('sitemap.xml')
