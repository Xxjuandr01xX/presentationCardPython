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
    ##Pagina principal 
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM py_profile_person WHERE id=1")
    data = cursor.fetchall()
    return render_template('home.html', perfil=data)

@app.route("/administrador")
def admin():
    ## Pagina para inicio de Session en Administrador
    pass
if __name__ == "__main__":
    app.run(port=3000, debug=True)