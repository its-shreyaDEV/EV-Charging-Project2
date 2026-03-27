# ⚡ Smart EV Charge Finder

A Flask web application that helps electric vehicle owners in India find nearby charging stations based on their current location and remaining battery level. It uses **KNN + KMeans machine learning** to cluster stations geographically and predict the best options within the vehicle's range.

---

## Features

* Battery-aware range calculation
* KNN nearest-station lookup (haversine distance)
* KMeans geographic clustering (15 zones)
* Random Forest demand scoring
* Interactive cluster map
* Location autocomplete (OpenCage API)
* User authentication (Werkzeug hashing)
* Admin panel

---

## Tech Stack

| Layer      | Technology                  |
| ---------- | --------------------------- |
| Backend    | Python, Flask               |
| ML/Data    | scikit-learn, pandas, numpy |
| Database   | SQLite                      |
| Frontend   | HTML, CSS, JS               |
| Deployment | Gunicorn                    |

---

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open:
http://127.0.0.1:5000

---

## Project Highlights

* 1500+ EV stations processed
* Real-time distance filtering using Haversine formula
* ML-based clustering + ranking
* Full-stack implementation

---

## Author

Shreya Dash
