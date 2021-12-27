from flask import Flask, request, render_template, Response, url_for, g
from sqlite3 import dbapi2 as sqlite3
from functools import wraps

app = Flask(__name__)

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(':memory:', isolation_level=None)
		db.row_factory = sqlite3.Row
		with app.app_context():
			db.cursor().execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT);')
			with app.open_resource('schema.sql', mode='r') as f:
				db.cursor().executescript(f.read())
	return db

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None: db.close()

def query_db(query, args=(), one=False):
	try:
		with app.app_context():
			cur = get_db().execute(query, args)
            # cur.fetchall() returns a list of list, each element is a row in the sql table
			rv = [dict((cur.description[idx][0], value) for idx, value in enumerate(row)) for row in cur.fetchall()]
			return (rv[0] if rv else None) if one else rv
	except Exception as e:
		return e

	return None

@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		q = "select * from users where username = '%s' AND password = '%s';" % (request.form.get('username', ''), request.form.get('password', ''))

		login = query_db(q, one=True)

		if isinstance(login, Exception):
			error = '%s : %s' % (login.__class__, login)
			return render_template('index.html', query=q, error=error, image=url_for('static', filename='images/dog.png'))

		if login is None:
			return render_template('index.html', query=q, image=url_for('static', filename='images/dog.png'))

		if login.get('username', '') == 'admin':
			return render_template('index.html', query=open('flag').read())

	return render_template('index.html')

@app.route('/debug')
def debug():
	return Response(open(__file__).read(), mimetype='text/plain')

if __name__ == '__main__':
	app.run('0.0.0.0', port=1337)