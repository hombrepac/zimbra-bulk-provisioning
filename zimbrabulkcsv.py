#!/bin/python
# Name: Zimbra Bulk Provision CSV Converter
# Description: Convert a CSV file to zmprov format for provision
# Author: Leonardo Gallego
# Original Perl: https://wiki.zimbra.com/wiki/Bulk_Provisioning#CSV_File_to_zmprov

import csv
import sys
import os

# Crear cuenta:
# ca uid@dominio clave
# Modificar cuenta (nombre)
# ma uid@dominio givenName "Nombres"
# Modificar cuenta (apellido)
# ma uid@dominio sn "Apellidos"
# Modificar cuenta (uid)
# ma uid@dominio cn "uid"
# Modificar displayname (Remitente)
# ma uid@dominio displayName "Nombres Apellidos"
# Modificar cambiar clave 
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


