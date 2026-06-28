from flask import Blueprint, render_template, request, redirect
from utils.db import get_connection

security_bp = Blueprint('security', __name__)

@security_bp.route('/security')
def security_checks():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            sc.*,
            p.name,
            f.flight_no
        FROM security_checks sc
        JOIN passengers p
            ON sc.passenger_id = p.id
        JOIN flights f
            ON sc.flight_id = f.id
    """)

    checks = cur.fetchall()

    conn.close()

    return render_template(
        'security/security_list.html',
        checks=checks
    )



@security_bp.route('/add-security')
def add_security():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM passengers")
    passengers = cur.fetchall()

    cur.execute("SELECT * FROM flights")
    flights = cur.fetchall()

    conn.close()

    return render_template(
        'security/add_security.html',
        passengers=passengers,
        flights=flights
    )


@security_bp.route(
    '/save-security',
    methods=['POST']
)
def save_security():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO security_checks(
            passenger_id,
            flight_id,
            baggage_scan,
            metal_detector,
            risk_level,
            security_status,
            officer_name,
            remarks
        )
        VALUES(?,?,?,?,?,?,?,?)
        """,
        (
            request.form['passenger_id'],
            request.form['flight_id'],
            request.form['baggage_scan'],
            request.form['metal_detector'],
            request.form['risk_level'],
            request.form['security_status'],
            request.form['officer_name'],
            request.form['remarks']
        )
    )

    conn.commit()
    conn.close()

    return redirect('/security')