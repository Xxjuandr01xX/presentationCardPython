from flask import Flask, render_template
from flask_mysqldb import MySQL
from module import funciones
import requests

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
    ## Inicio de session de administrador
    return render_template('login.html', title="Carta de presentacion", header="INICIAR SESSION")

@app.route("/loginuser", methods=['POST'])
def loginuser():
    #Funcion para validar datos de formulario de inicio de session.
    username = requests.form('usr')
    password = requests.form('pwd')
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM py_userse WHERE username='{}' AND passwd=PASSWORD('{}')".format(username, password))
    data = cursor.fetchall()
    pass

if __name__ == "__main__":
    app.run(port=3000, debug=True)