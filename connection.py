import mysql.connector, os, sys
from dotenv import load_dotenv
from mysql.connector import Error


class Conexion:

  def __init__(self):
    load_dotenv()

    self.tableTest = os.getenv('TABLE_TEST') or 'testing_python'

    self._config = {
      'host': os.getenv('HOST_DATABASE') or "localhost",
      'user': os.getenv('USER_DATABASE') or "root",
      'password': os.getenv('PASSWORD_DATABASE') or ""
    }
    

  def _abrirConexion(self):
    try:
      mydb = mysql.connector.connect(**self._config)
      return mydb
    except Error as e:
      print("No se encontro la base de datos")
      sys.exit(0)

  def mostrarDataBases(self):
    mydb = self._abrirConexion()
    db = mydb.cursor()
    db.execute("SHOW DATABASES")
    
    resutl = []
    for dbs in db:
      resutl.append(dbs[0])

    mydb.close()
    return resutl

  def crearDataBase(self, nombre="test"):
    mydb = self._abrirConexion()
    db = mydb.cursor()

    query = "CREATE DATABASE %s;" % nombre
    
    try:
      db.execute(query)
      mydb.commit()
      mydb.close()
      return True
    except:
      mydb.close()
      return False

  def crearTabla(self):
    mydb = self._abrirConexion()
    db = mydb.cursor()

    try:
      db.execute(f"CREATE TABLE {self.tableTest}" 
    "(id INT NOT NULL AUTO_INCREMENT,"
    "nombre VARCHAR (32) NOT NULL,"
    "edad INT,"
    "PRIMARY KEY (id));")
      mydb.commit()
      mydb.close()
      return True
    except Error as e:
      print(e)
      mydb.close()
      return False

  def agregarDatos(self, data):
    mydb = self._abrirConexion()
    db = mydb.cursor()

    query = (f"INSERT INTO {self.tableTest}(nombre, edad)" 
              "VALUES(%s, %s)") 

    try:
      db.execute(query, data)
      mydb.commit()
      mydb.close()
      return True
    except Error as e:
      print(e)
      mydb.close()
      return False

  def mostrarDatos(self):
    mydb = self._abrirConexion()
    db = mydb.cursor()

    query = (f"SELECT * FROM {self.tableTest}") 

    try:
      db.execute(query)
      result = db.fetchall()
      mydb.close()
      return result
    except Error as e:
      # print(e)
      mydb.close()
      return False

  def setConfig(self, db):
    self._config['database'] = db

