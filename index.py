from flask import Flask, render_template, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from module.funciones import *
from flask import request

app = Flask(__name__)
app.secret_key = "mysecretkey"
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
            cursor.execute("SELECT * FROM py_userse WHERE username=%s AND passwd=PASSWORD(%s)", (username, password))
            mysql.connection.commit()
            data = cursor.fetchall()
            if len(data) > 0:
                for person in data:
                    session["id_person"] = person[3]
                    session["id_rol"]    = person[4]
                session["username"]  = username
                return redirect(url_for("profile"))
            elif len(data) > 1:
                return "NULL"
            else:
                flash("Error al ingresar datos,compruebe y verifique !!")
                return redirect(url_for("admin"))
        else:
            flash("Asegurece de llenar los campos !!")
            return redirect(url_for("admin"))
    else:
        return "NULL"

##PERFIL
@app.route("/profile")
def profile():
    ## pagina donde se define el perfil del profesional.
    if session["id_person"]:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM py_profile_person WHERE id={}".format(session["id_person"]))
        mysql.connection.commit()
        data = cursor.fetchall()
        return render_template("profile_admin.html", username=session["username"], id=session["id_person"], profile=data)

@app.route("/update_profile/<string:id>", methods=["POST"])
def update_profile(id):
    if session["id_person"]:
        ##agregar validaciondes y mensajes.
        person_id = id
        nom  = request.form['nom'] 
        ape  = request.form['ape'] 
        mail = request.form['mail'] 
        telf = request.form['telf'] 
        prof = request.form['prof'] 
        fec  = request.form['fec_nac'] 
        dire = request.form['dir'] 
        cur = mysql.connection.cursor()
        cur.execute('''UPDATE py_profile 
                        SET nombre={},
                            apellido={},
                            correo={},
                            telefono={},
                            profesion={},
                            direccion={},
                            fec_nac={}
                        WHERE id={} '''.format(nom, ape, mail, telf, prof, dire, fec, person_id))
        mysql.connection.commit()
        flash("Perfil actualizado de manera exitosa !!")
        return redirect(url_for("profile"))

##Slider
@app.route("/slider")
def slider():
    ##Listado de imagenes para el carrusell de la pagina principal
    if session["id_person"]:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM py_slider")
        mysql.connection.commit()
        data = cur.fetchall()
        return render_template("sliders_list.html", slider=data)

@app.route("/del_slider/<string:id>")
def del_slider(id):
    ## Funcion para eliminar una imagen del slider.
    if session["id_person"]:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM py_slider WHERE id={}".format(id))
        mysql.connection.commit()
        flash("El slider ha sido Eliminaro Exitosamente")
        return redirect(url_for("slider"))



if __name__ == "__main__":
    app.run(port=3000, debug=True)