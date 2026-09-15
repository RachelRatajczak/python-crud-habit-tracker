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
