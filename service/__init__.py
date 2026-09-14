""" creates and configures flask applocation"""

import os
from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman
from flask_sqlalchemy import SQLAlchemy
from service.models import db

# Create Flask application
app = Flask(__name__)

# Application configuration
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URI",
    "sqlite:///accounts.db",
)

# Initialize database
db.init_app(app)

# Enable CORS
CORS(app)

# Add security headers
Talisman(app, force_https=False)

# Import routes after app creation
from service import routes  # noqa: E402,F401

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
