"""
app_logic.py

Defines all the app logic and helper functions for the Habit Tracker app.
Responsible for creating, updating, deleting, completing, and visualizing habit data.

Routes:
    - "/"              : Homepage view (GET/POST)
    - "/update"        : Rename a habit
    - "/delete"        : Delete a habit
    - "/complete/<id>" : Log today's completion for a habit
    - "/debug/logs"    : Show raw log data for debugging

Helper functions:
    - generate_habit_graph(): Generates progress graphs for each habit
    -
"""

from flask import render_template, request, redirect
from sqlalchemy.util import has_compiled_ext
from datetime import date, timedelta
from database import db, Habit, HabitLog
from database import db, Habit
import matplotlib
matplotlib.use("Agg")  # Use non-GUI backend for image generation
import matplotlib.pyplot as plt
import pandas as pd
import os


# Functions for the Habit objects
def register_routes(app):
    """
    The Flask routes for the Logic of the Habit Tracker app.
    """
    @app.route("/", methods=["GET", "POST"])
    def home():
        """
         Handles the homepage view for the habit tracker.

         - GET request:
            - Renders all existing habits.
            - Generates weekly progress graphs.

         - POST request:
            - Adds a new habit
            - Uses a redirect on page reload.
         """
        if request.method == "POST":
            title = request.form.get("title")
            if title:
                existing = Habit.query.filter_by(title=title).first()
                if not existing:
                    habit = Habit(title=title)
                    db.session.add(habit)
                    db.session.commit()
            return redirect("/")

        habits = Habit.query.all()

        habit_graphs = {}
        habit_week_data = {}

        for habit in habits:
            habit_graphs[habit.id] = generate_habit_graph(habit)
            habit_week_data[habit.id] = get_week_status(habit)
        return render_template("home.html", habits=habits, habit_graphs=habit_graphs, habit_week_data=habit_week_data)


    @app.route("/update", methods=["POST"])
    def update():
        """
        Updates a habit in the database.

        Request Form:
         - newtitle: New habit name
         - oldtitle: Existing habit name

        :return: Redirects to the homepage
        """
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        habit = Habit.query.filter_by(title=oldtitle).first()
        habit.title = newtitle
        db.session.commit()
        return redirect("/")


    @app.route("/delete", methods=["POST"])
    def delete():
        """
        Deletes a habit from the database.

        Request Form:
            - title: Title of the habit to delete

        :return: Redirects to the homepage
        """
        title = request.form.get("title")
        habit = Habit.query.filter_by(title=title).first()
        db.session.delete(habit)
        db.session.commit()
        return redirect("/")


    @app.route("/complete/<int:habit_id>", methods=["POST"])
    def complete(habit_id):
        """
        Logs today's completion for a given habit.

        Prevents duplicate entries for the same habit on the same date.

        Args:
            habit_id (int): The ID of the habit to log

        :return: Redirects to the homepage
        """
        today = date.today()

        # Check if today's log already exists
        existing_log = HabitLog.query.filter_by(habit_id=habit_id, date=today).first()
        if not existing_log:
            log = HabitLog(habit_id=habit_id, date=today)
            db.session.add(log)
            db.session.commit()
        return redirect("/")


    def get_week_status(habit):
        """
        Returns a dictionary showing which weekdays have been completed for a given habit.

        Args:
            habit (Habit): Habit object

        :return: Redirects to the homepage
        """
        today = date.today()
        start = today - timedelta(days=today.weekday())  # Monday of this week

        # Build dictionary: { 'Monday': True, 'Tuesday': False, ... }
        status = {}
        for i, day_name in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']):
            current_day = start + timedelta(days=i)
            log = HabitLog.query.filter_by(habit_id=habit.id, date=current_day).first()
            status[day_name] = bool(log)
        return status

    def generate_habit_graph(habit):
        """
        Creates a line graph showing daily completions for a specific habit.

        Saves the graph as a PNG file in the 'static/' folder.

          Args:
            habit (Habit): Habit object to visualize

        :return: Filename of the saved graph image
        """
        logs = HabitLog.query.filter_by(habit_id=habit.id).all()
        if not logs:
            return None  # Skip if no data

        # Count completions per day
        dates = [log.date for log in logs]
        df = pd.DataFrame({'date': dates})
        df['date'] = pd.to_datetime(df['date'])
        counts = df['date'].value_counts().sort_index()

        # Plot
        plt.figure(figsize=(4, 2))
        plt.plot(counts.index, counts.values, marker='o', color='blue')
        plt.title(habit.title)
        plt.xlabel("Date")
        plt.ylabel("Completions")
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save
        filename = f"{habit.title.replace(' ', '_')}_graph.png"
        filepath = os.path.join("static", filename)
        plt.savefig(filepath)
        plt.close()
        return filename


    # Testing
    @app.route("/debug/logs")
    def show_logs():
        """
        Displays all HabitLog entries for debugging.

        :return: HTML output of all HabitLog entries
        """
        logs = HabitLog.query.order_by(HabitLog.date.desc()).all()
        return "<br>".join([f"{log.habit.title} - {log.date}" for log in logs])


