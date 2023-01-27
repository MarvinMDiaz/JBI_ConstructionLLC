from flask import render_template, request, redirect, session, Flask
from flask_app import app
from flask import flash
import os
from flask_app.models.formValidation import User
from flask_mail import Mail, Message
from datetime import datetime
mail = Mail(app)


@app.route('/')
def homepage():
    current_year = datetime.now().year
    return render_template('Home.html', current_year=current_year)


@app.route('/submitted', methods=["POST"])
def contactForm():
    if not User.validate_form(request.form):
        print("Failed Validation")
        return redirect("/#Contact")
    else:
        print("Grabbing Form Details")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        print("grabbed form inputs")

        msg = Message(
            f"* New * Website E-mail from: {name}",
            sender="admin@jbiconstructionllc.com",
            recipients=["admin@jbiconstructionllc.com"]
        )

        msg.body = (
            f"\n\nClients Name: {name}\n\nEmail: {email}\n\nPhone Number: {phone}\n\nMessage: {message}")
        print("done with formatting email")
        print(msg)
        mail.send(msg)

        flash("Message was Succesfully sent ", "success")
        print("Message was Succesfully sent ")

    print("done")
    return redirect("/success")


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/sitemap.xml')
def sitemap():
    return render_template('sitemap.xml')
