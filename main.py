# Author: Yonatan Ortiz (kr4ken600)
# Date: 24/03/2023

from connection import Conexion
from sys import argv, exit
from colorama import init, Fore, Style

init()


def ayuda():
  print(Fore.RED + "\nForma de usar: python %s -cD [NOMBRE]" % argv[0])
  print(Fore.GREEN + "Comandos:")
  print("\t-sD:\t\tMostrar las bases de datos disponibles")
  print("\t-cD [NOMBRE]:\tCrear una base de datos")
  print("\t-cT [DATABASE]:\tCrear una tabla de pruebas")
  print("\t-iT [DATABASE]:\tInsertar datos en la tabla de pruebas")
  print("\t-sT [DATABASE]:\tMostrar datos de la tabla de pruebas")
  print("\t-h:\t\tAyuda")
  exit(0)

def menu():
  db = Conexion()
  if argv[1] == '-sD':
    for dbs in db.mostrarDataBases():
      print(Fore.BLUE + f"[-] {dbs}")
  elif argv[1] == '-cD':
    if len(argv) < 3:
      ayuda()

    if db.crearDataBase(argv[2]):
      print(Fore.GREEN + "[+] Base de datos creada con exito")
    else:
      print(Fore.RED + "[!] La base de datos ya existe o ocurrio un error inesperado")
  elif argv[1] == '-cT':
    if len(argv) < 3:
      ayuda()

    db.setConfig(argv[2])
    if db.crearTabla():
      print(Fore.GREEN + "[+] Tabla se creo con exito en la base de datos %s" % argv[2])
    else:
      print(Fore.RED + "[!] La tabla ya existe o ocurrio un error inesperado")
  elif argv[1] == '-iT':
    if len(argv) < 3:
      ayuda()

    db.setConfig(argv[2])
    nombre = input("Agrega tu nombre: ")
    edad = int(input("Agrega tu edad: "))

    if db.agregarDatos((nombre, edad)):
      print(Fore.GREEN + "[+] Se agregaron con exito los datos en la tabla de pruebas en la base de datos %s" % argv[2])
    else:
      print(Fore.RED + "[!] Ocurrio un error inesperado")
  elif argv[1] == '-sT':
    if len(argv) < 3:
      ayuda()
    
    db.setConfig(argv[2])

    if db.mostrarDatos() is False:
      print("No se encontro la tabla")

    print(Fore.BLUE +"--------------------------------")
    print("| ID \t| NOMBRE \t| EDAD |")
    print("--------------------------------")
    for data in db.mostrarDatos():
      id, nombre, edad = data
      print(f"| {id} \t| {nombre} \t|  {edad}  |")
    print("--------------------------------")
  elif argv[1] == '-h':
    ayuda()
  else:
    ayuda()
def main():
  if len(argv) < 2:
    ayuda()
  else:
    menu()

  print(Style.RESET_ALL)

if __name__ == "__main__":
  main()