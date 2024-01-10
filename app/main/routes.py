from app.main import bp
from flask import request, render_template, url_for, redirect, g
from app.auth import login_required
from app.db import select_all, select_one, execute_query
#Add what needs to be imported here. You probably need to rename that blueprint

@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/buttons')
def buttons():
    return render_template("buttons.html")

@bp.route('/cards')
def cards():
    return render_template("cards.html")

@bp.route('/charts')
def charts():
    return render_template("charts.html")

@bp.route('/forms')
def forms():
    return render_template("forms.html")

@bp.route('/modals')
def modals():
    return render_template("modals.html")

@bp.route('/tables')
def tables():
    return render_template("tables.html")

@bp.route('/connect')
def connect():
    return render_template("connect.php")

