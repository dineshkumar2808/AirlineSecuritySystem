from flask import Blueprint, render_template, request, redirect
from utils.db import get_connection

flight_bp = Blueprint('flight', __name__)


@flight_bp.route('/flights')
def flights():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM flights")
    flights = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        'flights/flight_list.html',
        flights=flights
    )


@flight_bp.route('/add-flight')
def add_flight():
    return render_template(
        'flights/add_flight.html'
    )


@flight_bp.route('/save-flight', methods=['POST'])
def save_flight():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO flights(
            flight_no,
            airline_name,
            source,
            destination,
            departure_time,
            arrival_time,
            status
        )
        VALUES(?,?,?,?,?,?,?)
        """,
        (
            request.form['flight_no'],
            request.form['airline_name'],
            request.form['source'],
            request.form['destination'],
            request.form['departure_time'],
            request.form['arrival_time'],
            request.form['status']
        )
    )

    conn.commit()
    cur.close()
    conn.close()

    return redirect('/flights')


@flight_bp.route('/edit-flight/<int:id>')
def edit_flight(id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM flights WHERE id=?",
        (id,)
    )

    flight = cur.fetchone()

    cur.close()
    conn.close()

    return render_template(
        'flights/edit_flight.html',
        flight=flight
    )


@flight_bp.route('/update-flight/<int:id>', methods=['POST'])
def update_flight(id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE flights
        SET flight_no=?,
            airline_name=?,
            source=?,
            destination=?,
            departure_time=?,
            arrival_time=?,
            status=?
        WHERE id=?
        """,
        (
            request.form['flight_no'],
            request.form['airline_name'],
            request.form['source'],
            request.form['destination'],
            request.form['departure_time'],
            request.form['arrival_time'],
            request.form['status'],
            id
        )
    )

    conn.commit()
    cur.close()
    conn.close()

    return redirect('/flights')


@flight_bp.route('/delete-flight/<int:id>')
def delete_flight(id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM flights WHERE id=?",
        (id,)
    )

    conn.commit()
    cur.close()
    conn.close()

    return redirect('/flights')