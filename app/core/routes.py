from app import app, db
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.core.forms import PostForm
from app.models import User, Post
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
    return render_template("core/index.html", form=form, posts=posts, images=images)
    #return "Hello World!"

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
    return render_template("core/profile.html", title="Profile", posts=posts, images=images)