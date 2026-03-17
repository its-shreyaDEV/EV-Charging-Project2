# ⚡ EV Charging Station Locator

<p align="center">
  <b>Find EV charging stations you can actually reach — not just the closest ones.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Backend-Flask-black?style=flat-square&logo=flask">
  <img src="https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-orange?style=flat-square">
  <img src="https://img.shields.io/badge/Database-SQLite-blue?style=flat-square">
  <img src="https://img.shields.io/badge/Data-Pandas-green?style=flat-square">
  <img src="https://img.shields.io/badge/API-Google%20Maps-red?style=flat-square&logo=googlemaps">
</p>

---

## 📌 Overview

As EV adoption accelerates in India, a critical usability gap remains:  
> Most platforms show nearby charging stations — but not whether you can actually reach them.

This project solves that by introducing a **battery-aware filtering system**, combining geolocation with real-world range estimation to surface only **reachable charging stations**.

Built using **Flask, SQLite, and Google Maps API**, this application demonstrates full-stack engineering — from backend architecture to interactive geospatial visualization.

---

## 🚀 Key Features

- 📍 **Real-Time Geolocation** — Detects user's live coordinates via browser  
- 🔋 **Battery-Aware Filtering** — Calculates reachable radius dynamically  
- 🗺️ **Interactive Map UI** — Google Maps integration with station markers  
- 🔐 **Authentication System** — Secure login & registration (hashed passwords)  
- 📊 **Data-Driven Backend** — EV dataset processed using Pandas  
- 💾 **Persistent Storage** — SQLite database for user data  

---

## 🖼️ Screenshots

> *(Add your screenshots here — this section is critical for recruiters)*

```md
![Home Page](./static/home.png)
![Map View](./static/map.png)
![Results](./static/results.png)
🛠️ Tech Stack
Layer	Technology
Frontend	HTML5, CSS3, JavaScript
Backend	Flask (Python)
Database	SQLite
Data Processing	Pandas
APIs	Google Maps JavaScript API
📂 Project Structure
EV-Charging-Locator/
│
├── app.py
├── database.py
├── requirements.txt
├── india_ev_charging_stations.csv
├── users.db
│
├── templates/
│   ├── home.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── result.html
│
└── static/
    ├── style.css
    ├── forecast.png
    └── stations.png
⚙️ Getting Started
Prerequisites

Python 3.10+

Google Maps API Key

Installation
git clone https://github.com/your-username/ev-charging-locator.git
cd ev-charging-locator

pip install -r requirements.txt
python app.py

Open in browser:

http://127.0.0.1:5000

⚠️ Add your Google Maps API key in the template before running.

🧠 How It Works
User Login
   ↓
Fetch Geolocation
   ↓
Input Battery %
   ↓
Calculate Range (battery × vehicle range)
   ↓
Apply Haversine Distance Filter
   ↓
Display Reachable Stations on Map

The system uses the Haversine formula to compute accurate great-circle distances between coordinates — ensuring precise filtering without relying on external routing APIs.

📊 Dataset

The application uses a curated dataset:
india_ev_charging_stations.csv

Includes:

Station names

Coordinates

Charger types

Operator details

Covers major Indian cities and highways.

🔐 Security

Password hashing (no plain-text storage)

Flask session-based authentication

Client + server-side validation

🔭 Roadmap

 Live charging station APIs integration

 Real-time availability tracking

 Route optimization & navigation

 Mobile/PWA version

 Charger-type filtering

 Cloud deployment (AWS / Render)

👨‍💻 Author

Shreya Dash
B.Tech Computer Science Engineering

🔗 LinkedIn

💻 GitHub

📄 License

This project is part of an academic portfolio.
Feel free to use and build upon it with proper attribution.

