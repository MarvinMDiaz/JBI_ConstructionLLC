JBI Construction
Welcome to the JBI Construction web application! This project is a Flask‐based website that integrates reCAPTCHA for form security, AWS SSM for securely managing secrets, and Amazon SES for sending emails.

(Replace the image link above with an actual banner if you have one.)

Table of Contents
Overview
Features
Tech Stack
Getting Started
Configuration
Deployment
Contributing
License
Overview
JBI Construction is a website showcasing construction services and providing a secure contact form. The site’s backend is built using the Flask framework, ensuring a modular MVC structure. It includes:

reCAPTCHA to protect contact forms from spam and bots.
AWS SSM to securely store and retrieve sensitive keys.
Amazon SES to reliably send emails (e.g., contact form submissions).
This repository contains all the code needed to run the site, from the Flask app logic to the front‐end templates and static assets.

Features
Contact Form with reCAPTCHA

Prevents spam and ensures legitimate user inquiries.
AWS SSM Parameter Store Integration

Retrieves secrets (like API keys, secret keys, etc.) at runtime, keeping them out of the codebase.
Email via Amazon SES

Sends email notifications when a user submits the contact form.
Nginx + Gunicorn Support

Easily deployable on an EC2 instance using a production‐ready web server stack.
Let’s Encrypt SSL (Optional)

Can integrate free SSL certificates with Certbot and auto‐renewal via cron.
Tech Stack
Backend: Python 3, Flask
Front‐End: HTML5, CSS3, JavaScript
AWS Services: Amazon SES, AWS SSM Parameter Store
Other Libraries: boto3, Flask-WTF, Gunicorn, Nginx
Getting Started
Prerequisites
Python 3.8+ installed
pip or pipenv for managing dependencies
(Optional) An AWS account if you want to integrate SSM and SES.
