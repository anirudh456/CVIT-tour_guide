
from runtime.config.config import Config
from runtime.rest.app import create_app
from runtime.config import flask_app_config as config
from runtime.utils.class_persistence_template import db
from runtime.system.system import System

if __name__ == "__main__":
    db.create_all(app=create_app(config))
    Config.populate_db()
