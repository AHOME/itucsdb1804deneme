from flask import current_app, render_template, request, redirect, url_for, session, flash
from flask_login import login_user, logout_user, login_required, current_user
from passlib.hash import pbkdf2_sha256 as hasher
from forms import LoginForm
from login import sign_up

def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.data["username"]
        db = current_app.config["db"]
        user = db.customer.get_row("*", "USERNAME", username)
        if user is not None:
            password = form.data["password"]
            remember = form.data["remember_me"]
            if hasher.verify(password, user.password_hash):
                login_user(user, remember)
                flash("You have logged in successfully", "success")
                next_page = request.args.get("next", url_for("home_page"))
                return redirect(next_page)

        flash("Invalid credentials.", "danger")
    return render_template("customer/login.html", form=form)


def logout_page():
    logout_user()
    flash("You have logged out.", "info")
    return redirect(url_for("home_page"))


def signup_page():
    if request.method == "GET":
        return render_template("customer/signup.html")
    else:
        u_username = request.form["inputUsername"]
        u_password = request.form["inputPassword"]
        u_email = request.form["inputEmail"]
        u_name = request.form["inputName"]
        u_surname = request.form["inputSurname"]
        u_phone = request.form["inputPhone"]
        u_DOB = request.form["inputDOB"]
        u_gender = request.form["inputGender"]

        sign_up(u_username, u_password, u_email, u_name, u_surname, u_phone, u_DOB, u_gender)
        flash("You have registered successfully", "success")
        return redirect(url_for("home_page"))