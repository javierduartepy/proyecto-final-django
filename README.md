# 🚀 Proyecto final de Django del Informatorio 2021

## Configuración del entorno de desarrollo

- Instalar [Visual Studio Code](https://code.visualstudio.com/download) como IDE.

### Extensiones Requeridas en VS Code

- [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
- [Python](https://github.com/Microsoft/vscode-python)

### Instalaciones obligatorias

- [Python 3.9](https://www.python.org/downloads/)

### Instalaciones de paquetes necesarios con pip de forma local

La configuracion de un entorno virtual queda a cargo de cada developer como quiera trabajar, las librerias necesarias que necesita tener instalado en su entorno local estan en el archvivo `requirements.txt` y se puede instalar directamente con este comando:

```
pip install -r requirements.txt
```

### [DEPRECADO] Pasos para configurar y corre el proyecto localmente en un entorno virtual

> Importante: Tenes Git instalado y configurado localmente con una public key SSH. Todos estos pasos se realizaran por linea de comandos.

En el repositorio se subio el archivo `Pipfile` que es la configuración del entorno virtual que estamos utilizando, por lo tanto lo unico que necesitamos hacer es:

1. Abrimos una consola (CMD), vamos a la unidad `C:/`.

2. Clonamos el proyecto con `git clone git@github.com:javierduartepy/proyecto-final-django.git`, esto nos crea un carpeta llamada `proyecto-final-django` con todo el contenido del proyecto.

3. Vamos por consola dentro de la carpeta del proyecto `cd proyecto-final-django` y corremos el siguiente comando `pipenv install`, esto crea el entorno virtual.

4. Activamos el entorno virtual con `pipenv shell`, este paso es necesario para ejecutar el proyecto de forma local.

5. Para ejecutar el proyecto de forma local entramos a la carpteta `cd QuizChacoApp` y ejecutamos el comando `python manage.py runserver`

> Nota: Si el pipenv no funciona se pueden instalar los paquetes de proyecto ejecutando el comando "pip install -r requirements.txt" dentro de la carpeta "QuizChacoApp"

6. En el navegador pegamos la url -> `http://127.0.0.1:8000/` y nos muestra la vista de Home
