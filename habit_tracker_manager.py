"""
habit_tracker.manager.py

Main entry point for the Habit Tracker web application.
Responsible for setting up the Flask application, configuring a database, and route registration.

Usage:
    Run -
        flask --app habit_tracker_manager run
    Change to the database -
        flask --app habit_tracker_manager db migrate -m "Descriptive message"
"""

from database import db
from flask import Flask
from flask_migrate import Migrate

# Create a Flask object
def create_app():
    """
    Create and configure the Flask application.
        - Sets up a SQLite database connection
        - Initializes Flask-Migrate for database migrations
        - Registers routes

    :return: Flask app object
    """
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///habit_data.db"
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    db.init_app(app)
    Migrate(app, db)

    with app.app_context():
        from app_logic import register_routes
        register_routes(app)

    return app

app = create_app()

# Networking: Location of the web application
if __name__ == "__main__":
    """
    Runs the Flask application on a development server.
    
    The server is accessible at http://0.0.0.0.0:5000/
    """
    app.run(host="0.0.0.0", port=5000, debug=True)


