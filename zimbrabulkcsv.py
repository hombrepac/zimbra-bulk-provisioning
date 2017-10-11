#!/bin/python

import csv
import sys
import os

# ca uid@dominio clave
# ma uid@dominio givenName "Nombres"
# ma uid@dominio sn "Apellidos"
# ma uid@dominio cn "uid"
# ma uid@dominio displayName "Nombres Apellidos"
# ma uid@dominio zimbraPasswordMustChange TRUE

archivo = sys.argv[1]
dominio = sys.argv[2]

def csv_dict_reader(file_obj):
    lineas = csv.DictReader(file_obj, delimiter=';')
    for linea in lineas:
        print("createAccount"),
        print(linea["uid"]+ "@" + dominio),
        print(linea["password"]),
        print("displayName"),
        print(linea["givenname"] + " " + linea["sn"]),
        print("givenName"),
        print(linea["givenname"]),
        print("sn"),
        print(linea["sn"])

if __name__ == "__main__":
#    with open("correos.csv") as f_obj:
    if ( not os.path.isfile( archivo ) ):
            print ("Error, el archivo no existe: " % archivo)
            print ("debe ingresar un archivo csv valido")
    else:
        with open(archivo) as f_obj:
            csv_dict_reader(f_obj)


