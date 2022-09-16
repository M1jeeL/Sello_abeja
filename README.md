# Sello abeja

# Iniciar entorno virtual [venv]

1.- Dirigirse a la Carpeta "selloabeja" [CMD o VScode]

    -> C:\Users\XXXXX\Desktop\selloabeja

2.- Escribir en la consola

    Entiendase por el segundo 'venv' es el nombre del entorno virtual el cual estamos creando.
    -> python -m venv venv

3.- Activar entorno virtual

    Entrar a la carpeta Scripts.
    -> cd venv\Scripts
    Escribir en consola.
    -> activate
    Listo!

    Para desactivar el entorno virtual
    -> (venv) C:\Users\XXXXX\Desktop\selloabeja\venv\Scripts> deactivate

    [!]IMPORTANTE: Si les tira algun error por consola, hacerlo desde CMD y no de PS. (Para entrar a la CMD deben escribir cmd en consola y listo)

4.- Instalacion de los requirements

    Volver al directorio principal.
    -> cd ..\..\ ó cd C:\Users\XXXXX\Desktop\selloabeja
    Escribir en consola.
    -> pip install -r requirements.txt
    Listo!

    [!]IMPORTANTE: Si llegasen a instalar alguna libreria, despues de instalarla escribir en consola 'pip freeze' y copiar todo y pegarlo en requirements.txt (Informar esto en el commit)

5.- Habilitacion del Entorno Django

    Descripcion de comandos globales:
    -> python manage.py runserver [Encender el servidor]
    -> python manage.py makemigrations [Corrobora si hay cambios o no en el modelo]
    -> python manage.py migrate [Realiza las migraciones]
    -> python manage.py createsuperuser [Crea el usuario ADMIN del administrador de Django]

    Primer paso: Hacer un makemigrations
    Entrar al directorio selloabeja
    -> (venv) C:\Users\XXXXX\Desktop\selloabeja> cd backendapp
    Escribir el comando de Makemigrations
    -> (venv) C:\Users\XXXXX\Desktop\selloabeja\selloabeja> python manage.py makemigrations

    Segundo paso: Realizar las migraciones
    Escribir el comando Migrate
    -> (venv) C:\Users\XXXXX\Desktop\selloabeja\selloabeja> python manage.py migrate

    Tercer paso: Creacion del SuperUsuario
    Escribir el comando Createsuperuser
    -> (venv) C:\Users\XXXXX\Desktop\selloabeja\selloabeja> python manage.py createsuperuser
    *Rellenar los valores por defecto*

    Cuarto paso: Encender el servidor
    Escribir el comando runserver
    -> (venv) C:\Users\XXXXX\Desktop\selloabeja\selloabeja> python manage.py runserver

# Variables de entorno
SECRET_KEY=<my_secret_key>

POSTGRESQL_NAME=<posgresql_database>

POSTGRESQL_USER=<posgresql_user>

POSTGRESQL_PASS=<postgresql_pass>

POSTGRESQL_HOST=localhost

POSTGRESQL_PORT=5432

DEBUG=True
