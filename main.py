
# python3

__version__='0.0.0-1'

from app import app
from flask import request
from flask import jsonify

from db import mysql


@app.route("/", methods=['GET'])
def root():
    return jsonify(status=200, message="OK", version=__version__), 200

@app.route("/mysql/user", methods=['GET'])
def mysql_user():
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM mysql.user;")
    rows = cur.fetchall()
    resp = jsonify(rows)
    cur.close()
    conn.close()
    return resp, 200


@app.errorhandler(404)
def not_found(error=None):
    message = { 'status': 404, 'message': 'Not Found: ' + request.url }
    #resp = jsonify(message)
    #resp.status_code=404
    #return resp
    return jsonify(message), 404

if __name__ == "__main__":
    app.run(port=8980, debug=False)


