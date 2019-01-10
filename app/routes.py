from flask_site import app, db
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.forms import LoginForm, RegistrationForm, PostForm
from app.models import User, Post

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
    return render_template("index.html", form=form, posts=posts)
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