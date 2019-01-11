from flask import render_template
from app import db
from app.errors import bp

@bp.app_errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404

@bp.app_errorhandler(500)
def big_error(e):
    db.session.rollback()
    return render_template("errors/500.html"), 500