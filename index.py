from flask import Flask, render_template, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from module.funciones import *
from flask import request
from werkzeug.utils import secure_filename
from os import remove
import os

app = Flask(__name__)
app.secret_key = "mysecretkey"
app.config["UPLOAD_FOLDER"] = "static/img/slides"
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
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM py_slides")
    s = cur.fetchall()
    return render_template('home.html', perfil=data, slides=s)

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
    ## Funcion para actualizar informacion de perfil de usuario
    if session["id_person"]:
        if request.method == "POST":
            nom  = request.form['nom'] 
            ape  = request.form['ape'] 
            mail = request.form['mail'] 
            telf = request.form['telf'] 
            prof = request.form['prof'] 
            fec  = date_to_sql(request.form['fec_nac']) 
            dire = request.form['dir']
            ##Validaciones de campos de texto
            if nom == "":
                flash("Asegurece de agregar su nombre !")
                return redirect(url_for("/profile"))
            elif ape == "":
                flash("Asegurece de agregar su apellido !")
                return redirect(url_for("/profile"))
            elif mail == "":
                flash("Asegurece de agregar su correo electronico !")
                return redirect(url_for("/profile"))
            elif telf == "":
                flash("Asegurece de agregar su telefono !")
                return redirect(url_for("/profile"))
            elif prof == "":
                flash("Asegurece de agregar su profesion !")
                return redirect(url_for("/profile"))
            elif fec == "":
                flash("Asegurece de agregar su Fecha de necimiento !")
                return redirect(url_for("/profile"))
            elif dire == "":
                flash("Asegurece de agregar su Direccion !")
                return redirect(url_for("/profile"))
            else:
                cur = mysql.connection.cursor()
                cur.execute('''UPDATE py_profile_person 
                                SET nombre='{}',
                                    apellido='{}',
                                    correo='{}',
                                    telefono='{}',
                                    profesion='{}',
                                    direccion='{}',
                                    fec_nac='{}'
                                WHERE id={} '''.format(nom, ape, mail, telf, prof, dire, fec, id))
                mysql.connection.commit()
                flash("Perfil actualizado de manera exitosa !!")
                return redirect(url_for("profile"))

##Slider
@app.route("/slider")
def slider():
    ##Listado de imagenes para el carrusell de la pagina principal
    if session["id_person"]:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM py_slides")
        mysql.connection.commit()
        data = cur.fetchall()
        return render_template("sliders_list.html", slider=data)

@app.route("/del_slide/<string:id>")
def del_slide(id):
    ## Funcion para eliminar una imagen del slider.
    if session["id_person"]:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM py_slides WHERE id={}".format(id))
        data = cur.fetchall()
        for img in data:
            remove(img[2])
        cur2 = mysql.connection.cursor()
        query = cur2.execute("DELETE FROM py_slides WHERE id={}".format(id))
        mysql.connection.commit()
        if query:
            flash("Slide Eliminado Exitosamente !!")
            return redirect(url_for("slides"))

@app.route("/add_slider")
def add_slider():
    ## Formulario para registrar una nueva imagen para el slider.
    if session["id_person"]:
        return render_template("add_slider.html")

@app.route("/save_slides", methods=["POST"])
def save_slides():
    ## para guardar una imegen dentro del server y la db.
    if session["id_person"]:
        if request.method == "POST":
            file = request.files["f_content"]
            filename = secure_filename(file.filename)
            if filename == "":
                flash("Debe de cargar una imagen para continuar.")
                redirect(url_for("slider"))
            else:
                path_img = app.config["UPLOAD_FOLDER"]+"/"+filename
                cur = mysql.connection.cursor()
                titulo_archivo = request.form["f_name"]
                cur.execute("INSERT INTO py_slides (id, title, dir_image)values(NULL,'{}','{}')".format(titulo_archivo, path_img))
                mysql.connection.commit()
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                flash("Imagen agregada exitosamente !!")
                return redirect(url_for("slider"))
@app.route("/logout")
def logout():
    ## Funcion para cerrar session
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(port=3000, debug=True)