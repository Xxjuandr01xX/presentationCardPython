from flask import Flask, render_template
from flask_mysqldb import MySQL
from module import funciones

app = Flask(__name__)
##Mysql params
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "pyprofile"
##Mysql connection
mysql = MySQL(app)


@app.route("/")
def home():
    return render_template('index_profile.html')

if __name__ == "__main__":
    app.run(port=3000, debug=True)