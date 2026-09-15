"""
database.py

Defines the SQLAlchemy database and models for the Habit Tracker app.

Includes:
    Habit - User-created habits
    HabitLog: Completion records for the habits on specific dates
"""

from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy database instance
db = SQLAlchemy()


class Habit(db.Model):
    """
    Represents a habit created by the user.

    Fields:
        id (int): The id of the habit
        title (str): The title of the habit

    Relationships:
        logs(List[HabitLog]): List of completed habit logs
            Automatically removed if a habit is deleted
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)

    # Automatically delete logs when a habit is deleted
    logs = db.relationship('HabitLog', backref='habit_ref', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Habit {self.title}>"


class HabitLog(db.Model):
    """
    Represents an instance of a completed habit.

    Fields:
        id (int): Primary key of the habit log
        habit_id (int): Foreign key reference to the habit
        date (date): Date of completed habit

    Notes:
        Tracks the completion of a habit on a specific date.
        Each log references a Habit by foreign key.
    """
    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)

