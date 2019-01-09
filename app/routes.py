from flask_site import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")
    #return "Hello World!"
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
