## Dependencias Mysql client
Instalar dependencias en el SO para trabajar con mysql 
> `sudo apt-get install python-dev default-libmysqlclient-dev # Debian / Ubuntu`

> `sudo yum install python-devel mysql-devel # Red Hat / CentOS`

> `brew install mysql-client # macOS (Homebrew)`

## Entorno virtual - python 3
Instalar dependencia para entornos virtuales
> `sudo apt-get install python3-venv`
>
Crear entorno de virtualización para dependencias
> `python3 -m  venv venv`

Ejecutar entorno de virtualización para dependencias
> `. venv/bin/activate`

Desactivar entorno de virtualización para dependencias
> `deactivate`

## Frezear e instalar dependencias
Freezear dependencias en archivo requirements
> `pip freeze > requirements.txt`

Instalar dependencias 
> `pip install -r requirements.txt`

## Flask
Iniciar flask
> `export FLASK_ENV=development`

> `flask run`