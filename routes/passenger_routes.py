from flask import Blueprint, render_template, request, redirect
from utils.db import get_connection

passenger_bp = Blueprint('passenger', __name__)

# View All Passengers
@passenger_bp.route('/passengers')
def passengers():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM passengers")
    passengers = cur.fetchall()

    conn.close()

    return render_template(
        'passengers/passenger_list.html',
        passengers=passengers
    )


# Add Passenger Page
@passenger_bp.route('/add-passenger')
def add_passenger_page():
    return render_template(
        'passengers/add_passenger.html'
    )


# Save Passenger
@passenger_bp.route('/save-passenger', methods=['POST'])
def save_passenger():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO passengers(
            name,
            passport_no,
            nationality,
            gender,
            phone,
            email
        )
        VALUES(?,?,?,?,?,?)
        """,
        (
            request.form['name'],
            request.form['passport_no'],
            request.form['nationality'],
            request.form['gender'],
            request.form['phone'],
            request.form['email']
        )
    )

    conn.commit()
    conn.close()

    return redirect('/passengers')


# Edit Passenger Page
@passenger_bp.route('/edit-passenger/<int:id>')
def edit_passenger(id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM passengers WHERE id=?",
        (id,)
    )

    passenger = cur.fetchone()

    conn.close()

    return render_template(
        'passengers/edit_passenger.html',
        passenger=passenger
    )


# Update Passenger
@passenger_bp.route('/update-passenger/<int:id>', methods=['POST'])
def update_passenger(id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE passengers
        SET
            name=?,
            passport_no=?,
            nationality=?,
            gender=?,
            phone=?,
            email=?
        WHERE id=?
        """,
        (
            request.form['name'],
            request.form['passport_no'],
            request.form['nationality'],
            request.form['gender'],
            request.form['phone'],
            request.form['email'],
            id
        )
    )

    conn.commit()
    conn.close()

    return redirect('/passengers')


# Delete Passenger
@passenger_bp.route('/delete-passenger/<int:id>')
def delete_passenger(id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM passengers WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/passengers')