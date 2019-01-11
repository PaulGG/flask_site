from flask_site import app, db
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm, RegistrationForm, PostForm, ResetPasswordForm, ResetPasswordRequestForm
from app.models import User, Post
from app.email import send_password_reset_email
import re
import copy

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post_box.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Post successful.", "success")
        return redirect(url_for("index"))
    posts = reversed(Post.query.all())
    posts_iterable = copy.copy(posts)
    images = {}
    for p in posts_iterable:
        links = re.findall(r'(?:http\:|https\:)?\/\/.*\.(?:png|jpg|PNG|JPG|jpeg|JPEG)', p.body)
        images[p] = links
    return render_template("index.html", form=form, posts=posts, images=images)
    #return "Hello World!"
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password", "error")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash("Login successful for user {}.".format(form.username.data), "success")
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered.', "success")
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("You have successfully logged out.", "success")
    return redirect(url_for('index'))

@app.route("/user/<username>")
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = reversed(list(user.posts))
    posts_iterable = copy.copy(posts)
    images = {}
    for p in posts_iterable:
        links = re.findall(r"(https?://[^\s]+)", p.body)
        images[p] = links
    return render_template("profile.html", title="Profile", posts=posts, images=images)

@app.route("/reset_password_request", methods=["GET", "POST"])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash("Please check your email to reset your password.", "success")
        return redirect(url_for("login"))
    return render_template("reset_password_request.html", title="Reset Password", form=form)

@app.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for("index"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash("Your password has been successfully reset.", "success")
        return redirect(url_for("login"))
    return render_template("reset_password.html", form=form)
