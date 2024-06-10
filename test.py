from flask import Flask 
from flask_mysqldb import MySQL 
 
app = Flask(__name__) 
app.config['MYSQL_HOST'] = 'localhost:3306' 
app.config['MYSQL_USER'] = 'root' 
app.config['MYSQL_PASSWORD'] = '789789456qweQ$' 
app.config['MYSQL_DB'] = 'anime' 
 
mysql = MySQL(app) 
mysql.init_app(app)
 
@app.route('/') 
def users(): 
    cur = mysql.connection.cursor() 
    cur.execute("SELECT * FROM anime where id = 1") 
    rv = cur.fetchall() 
    return str(rv)