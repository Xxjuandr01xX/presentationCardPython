from flask import Flask, render_template
from flask_mysqldb import MySQL
from module.funciones import *
from flask import request

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
    if request.method == 'POST':
        username = request.form['usr']
        password = request.form['pwd']
        if string_null(username) != False and string_null(password) != False:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM py_userse WHERE username='{}' AND passwd=PASSWORD('{}')".format(username, password))
            data = cursor.fetchall()
            if len(data) > 0:
                return "Esto ya funciono !!"
            elif len(data) > 1:
                return "NULL"
            else:
                return render_template('login.html', mensage="Error al ingresar los datos, intente nuevamente. !!")
        else:
            return render_template('login.html', mensage="Asegurece de llenar los campo. !!")
    else:
        return "NULL"


if __name__ == "__main__":
    app.run(port=3000, debug=True)