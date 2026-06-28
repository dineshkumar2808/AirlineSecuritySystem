from flask import Blueprint, render_template, request, redirect, session
from utils.db import get_connection

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def login_page():
    return render_template('login.html')


@auth_bp.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT *
        FROM users
        WHERE username = ?
        AND password = ?
        """,
        (username, password)
    )

    user = cur.fetchone()

    cur.close()
    conn.close()

    if user:
        session['user'] = username
        return redirect('/dashboard')

    return "Invalid Credentials"


# @auth_bp.route('/dashboard')
# def dashboard():

#     if 'user' not in session:
#         return redirect('/')

#     return render_template('dashboard.html')
# from flask import Blueprint, render_template, request, redirect, session
# from utils.db import get_connection

# auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/dashboard')
def dashboard():

    if 'user' not in session:
        return redirect('/')

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM passengers")
    passenger_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM flights")
    flight_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM security_checks")
    security_count = cur.fetchone()[0]

    conn.close()

    return render_template(
        'dashboard.html',
        passenger_count=passenger_count,
        flight_count=flight_count,
        security_count=security_count
    )


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@auth_bp.route('/register')
def register_page():

    if 'user' in session:
        return redirect('/dashboard')

    return render_template('register.html')

@auth_bp.route('/save-user', methods=['POST'])
def save_user():

    username = request.form['username']
    password = request.form['password']
    role = request.form['role']

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO users(
            username,
            password,
            role
        )
        VALUES(?, ?, ?)
        """,
        (
            username,
            password,
            role
        )
    )

    conn.commit()
    conn.close()

    return redirect('/')