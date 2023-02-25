# Script para conectar con MySQL desde Python

Un script sencillo que puede realizar sentencias consultas de MySQL.
***
## Instalación
```
git clone https://github.com/kr4ken600/python-mysql.git
cd python-mysql
pip install -r requirements.txt
```
Recuerda crear un entorno virtual y tu respectivo archivo *.env* con las siguientes variables:
> HOST_DATABASE

> USER_DATABASE

> PASSWORD_DATABASE

> TABLE_TEST

De lo contrario hara uso de un servicio local.

El archivo *main.py* contiene el flujo del script. Mientras que *connection.py* contiene la conexion y las consultas MySQL.

***
## Forma de usar
Usar este script es muy sencillo, ya que hace uso de argumentos.
### Ayuda
```
python main.py -h
```
![Image Text](/imgs/1.png)
### Listar Base de Datos
```
python main.py -sD
```
![Image Text](/imgs/2.png)
### Crear una Base de Datos
```
python main.py -cD [NOMBRE]
```
![Image Text](/imgs/3.png)
![Image Text](/imgs/4.png)
### Crear una Tabla en una Base de Datos especifica y mostrar sus datos
```
python main.py -cT [DATABASE]
python main.py -sT [DATABASE]
```
![Image Text](/imgs/5.png)
![Image Text](/imgs/6.png)

### Ingresar Datos a la Tabla en una Base de Datos especifica
```
python main.py -iT [DATABASE]
```
![Image Text](/imgs/7.png)
![Image Text](/imgs/8.png)
