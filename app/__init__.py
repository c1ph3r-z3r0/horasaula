import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Caminho absoluto da pasta base do projeto
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Caminho absoluto para o arquivo do banco SQLite
    db_path = os.path.join(base_dir, 'instance', 'escola.db')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Importações internas (depois do app/db)
    from app import routes, models

    return app
