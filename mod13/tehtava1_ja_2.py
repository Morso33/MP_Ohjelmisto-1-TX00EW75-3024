from flask import Flask, jsonify
import mariadb
import math

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/alkuluku/<int:number>', methods=['GET'])
def prime_check(number):
    return jsonify({"Number": number, "isPrime": is_prime(number)})

@app.route('/kentta/<icao>', methods=['GET'])
def airport_info(icao):
    global con
    cur = con.cursor()
    query = """
            SELECT
                name, municipality
            FROM    
                airport
            WHERE
                ident = ?
        """
    cur.execute(query, (icao.upper(),))
    row = cur.fetchone()
    if row:
        return jsonify({"ICAO": icao.upper(), "Name": row[0], "Municipality": row[1]})
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    con = mariadb.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='metropolia',
        password='metropolia',
        autocommit=True
    )
    app.run(debug=True, port=3000)
