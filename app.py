from flask import Flask

app = Flask(__name__)

app.secret_key = "airline_security_secret"

from routes.auth_routes import auth_bp

app.register_blueprint(auth_bp)


from routes.passenger_routes import passenger_bp

app.register_blueprint(passenger_bp)

from routes.flight_routes import flight_bp

app.register_blueprint(flight_bp)

from routes.security_routes import security_bp

app.register_blueprint(security_bp)



if __name__ == "__main__":
    app.run(debug=True)

