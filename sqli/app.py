from flask import Flask, render_template, request, g
from flask_bootstrap import Bootstrap5
import sqlite3

app = Flask(__name__)
bootstrap = Bootstrap5(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('./db.sqlite')
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/', methods=['GET'])
def index():
    cur = get_db().cursor()
    cur.row_factory = sqlite3.Row
    if 'name' in request.args:
        name = request.args['name']
        query = f'SELECT * FROM Books where name LIKE \'%{name}%\''
    else:
        query = 'SELECT * FROM Books'

    app.logger.info(query)
    res = cur.execute(query)
    data = res.fetchall()

    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8301, debug=False)
