# Code provided by HBO-ICT
from flask import Flask
from app.db import read_db_config, close_db

def create_app():
    app = Flask(__name__)
    app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True
    app.config['SECRET_KEY'] = 'MYVERYLONGSECRET'
    app.config['MYSQL_CONFIG'] = read_db_config('instance/db.config')

    app.teardown_appcontext(close_db)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # You should probably configure your own blueprint here:
    #from app.MYBLUEPRINT import bp as events_bp
    #app.register_blueprint(MYBLUEPRINT.bp, url_prefix='/MYBLUEPRINT')

    return app
