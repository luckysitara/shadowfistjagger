from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt
from .routes import auth, project, bug, bounty

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(project.bp)
    app.register_blueprint(bug.bp)
    app.register_blueprint(bounty.bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
