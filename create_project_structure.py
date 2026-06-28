import os

folders = [
    "database",

    "models",
    "routes",
    "templates",

    "templates/passengers",
    "templates/flights",
    "templates/security",
    "templates/watchlist",
    "templates/incidents",

    "static",
    "static/css",
    "static/js",
    "static/images",
    "static/uploads",
    "static/uploads/passports",
    "static/uploads/documents",

    "utils",
    "reports"
]

files = [
    "app.py",
    "config.py",
    "requirements.txt",

    "database/airline_security.sql",

    "models/user_model.py",
    "models/passenger_model.py",
    "models/flight_model.py",
    "models/security_model.py",
    "models/watchlist_model.py",
    "models/incident_model.py",

    "routes/auth_routes.py",
    "routes/dashboard_routes.py",
    "routes/passenger_routes.py",
    "routes/flight_routes.py",
    "routes/security_routes.py",
    "routes/watchlist_routes.py",
    "routes/incident_routes.py",

    "templates/login.html",
    "templates/dashboard.html",

    "templates/passengers/passenger_list.html",
    "templates/passengers/add_passenger.html",
    "templates/passengers/edit_passenger.html",

    "templates/flights/flight_list.html",
    "templates/flights/add_flight.html",
    "templates/flights/edit_flight.html",

    "templates/security/screening_list.html",
    "templates/security/add_screening.html",

    "templates/watchlist/watchlist.html",
    "templates/watchlist/add_watchlist.html",

    "templates/incidents/incident_list.html",
    "templates/incidents/add_incident.html",

    "static/css/style.css",
    "static/css/login.css",
    "static/css/dashboard.css",

    "static/js/validation.js",
    "static/js/dashboard.js",
    "static/js/alerts.js",

    "utils/db.py",
    "utils/auth.py",
    "utils/validators.py",
    "utils/watchlist_checker.py",

    "reports/passenger_reports.py",
    "reports/security_reports.py",
    "reports/incident_reports.py"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file in files:
    with open(file, "w") as f:
        pass

print("✅ Airline Security System project structure created successfully!")