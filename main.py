from flask import Flask, render_template,json,jsonify
from flask.ext.mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'
mysql = MySQL(app)

@app.route('/')
def index():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM country''')
	wishes = cur.fetchall()
	wishes_dict = []
	for wish in wishes:
		wish_dict = {'name': wish[1],'population': wish[2]}
		wishes_dict.append(wish_dict)
	dataa=json.dumps(wishes_dict)
	return render_template("index.html",dataa=dataa)

if __name__ == '__main__':
	app.run(debug=True)