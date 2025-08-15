from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-change-me'

    # extensions
    bootstrap.init_app(app)

    # blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app