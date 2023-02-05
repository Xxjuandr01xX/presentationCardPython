def parse_string(string):
    #funcion para validar cadenas de caracteres
    pass

def string_null(string):
    if len(string) < 1:
        return False
    else:
        return string

def allowed_extensions(filename):
    allowed = ["jpg","jpeg","png"]
    fil = filename.split(".")
    if fil[1] in allowed:
        return True
    else:
        return False

def date_to_sql(date):
    ## para convertir el formato de fecha a formato sql
    convert = date.split("/")
    return "{}-{}-{}".format(convert[2], convert[1], convert[0])