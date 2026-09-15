Flask CRUD Application - Wellness and Habit Tracker
Author: Rachel Ratajczak 

Description:

A web-based habit tracker built using Flask, SQLAlchemy, and Matplotlib. 
Users can create, update, and delete habits, log daily completions, and visualize their progress over time. 
This project was created as part of the final assignment for the Python programming course at the University of Illinois Springfield.

Features:

- Add and manage custom habits 
- Log completion status per day
- Weekly progress view with checkboxes that reset every week
- Graphs to show habit completion trends over time 
- Persistent data using SQLite and SQLAlchemy 


Installation Instructions:

Needed: 
Python 3.9+
Teminal

1. Download the provided zip file ratajczak_habit_tracker.zip
2. Navigate to where the folder is located 
3. Create a virtual environment 
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate         # Windows
4. Install dependencies 
   pip install -r requirements.txt
5. Initialize the Database 
flask shell
    >>> from habit_tracker_manager import app, db
    >>> with app.app_context():
...     db.create_all()
    >>> exit()
6. Launch app
   flask --app habit_tracker_manager run
7. Visit http://127.0.0.1:5000 in a browser to start using the Habit Tracker.

How to Run:

1. Activate a virtual environment on your local terminal
   source .venv/bin/activate # for macOS/Linux 
   .venv\Scripts\activate # for Windows

2. Install necessary dependencies:
   pip install -r requirements.txt

3. Start the Flask development server 
   flask --app habit_tracker_manager run

4. Open the web app in a web browser (flask: port 5000)
   http://127.0.0.1:5000


Usage Examples:

Typical usage for a user:
- Start the app using the How to Run instructions. 
  - Create a new habit 
    - Type "yoga" or "walk" into the form and hit "Add Habit"
  - Track completion
    - Click "Mark Completed Today"
    - See check boxes and graphs to reflect progress
  - Visualize status 
    - Graphs automatically update to show trends 


Tech stack:

- Flask: web framework 
- SQLAlchemy:  database models 
- Pandas: organize completed data 
- Matplotlib: graphing data
- SQLite - database 


Troubleshooting:

Graphs not appearing?
  - If the progress graphs are not showing up, make sure the Matplotlib module is present in the environment
      pip install matplotlib
  - Make sure there is a static/ folder present - this is where the PNG habit graphs are saved
      mkdir static
    - macOS issue "NSWindow should only be instantiated on the main thread" - Matplotlib is trying to use a GUI backend
        import matplotlib
        matplotlib.use("Agg") # server side image generation 

ModuleNotFoundError?
  - Make sure the virtual environment is activated 
    source .venv/bin/activate
  - Make sure all the dependencies are installed
    pip install -r requirements.txt
