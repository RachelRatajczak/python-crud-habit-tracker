# Flask Wellness & Habit Tracker

A web-based habit tracker application built with Flask, SQLAlchemy, and Matplotlib to manage daily routines, log progress, and visualize behavioral trends over time. Developed as part of coursework at the University of Illinois Springfield.

---

## 🚀 Overview

This application enables users to establish personal wellness goals, track daily completion metrics, and maintain accountability through structured check-ins. It features persistent SQLite data storage, automated weekly resets, and dynamic server-side data visualizations generated via Matplotlib.

---

## ✨ Features

* **Habit Management:** Create, update, and delete custom daily habits.
* **Interactive Tracking:** Log daily completion status using a responsive interface with weekly reset functionality.
* **Data Visualization:** Automatically generate and display progress trends over time using Matplotlib.
* **Persistent Storage:** Safely store user data and habit states using SQLite and SQLAlchemy ORM.

---

## 🛠️ Tech Stack

* **Backend Framework:** Flask, Python 3.9+
* **Database & ORM:** SQLite, Flask-SQLAlchemy
* **Data Handling & Visualization:** Pandas, Matplotlib (Agg backend for server-side rendering)

---

## 📦 Installation & Setup

1. **Clone or download** the project folder locally and navigate into it via your terminal.
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS / Linux
   venv\Scripts\activate         # Windows


Install dependencies:

Bash
pip install -r requirements.txt
Initialize the Database:

Bash
flask shell
Once inside the Python/Flask shell, run:

Python
from habit_tracker_manager import app, db
with app.app_context():
    db.create_all()
exit()


How to Run
Activate your virtual environment on your local terminal:

Bash
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
Start the Flask development server:

Bash
flask --app habit_tracker_manager run
Open the web app: Navigate to http://127.0.0.1:5000 in your web browser.

Usage Example
Create a new habit: Type a habit like "yoga" or "walk" into the form and click Add Habit.

Track completion: Click Mark Completed Today to update your daily status. Checkboxes and graphs will reflect your progress.

Visualize status: Graphs automatically update to show your ongoing trends.

Troubleshooting
Graphs not appearing?

Make sure the Matplotlib module is installed: pip install matplotlib

Ensure a static/ folder is present in your root directory (where PNG habit graphs are saved): mkdir static

macOS GUI error ("NSWindow should only be instantiated on the main thread"): Ensure your code configures Matplotlib for server-side image generation:

Python
import matplotlib
matplotlib.use("Agg")
ModuleNotFoundError?

Verify your virtual environment is active: source venv/bin/activate

Ensure dependencies are installed: pip install -r requirements.txt
