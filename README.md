# Sistema de autenticación de usuarios

Aplicación web para el registro y autenticación, el cual permitirá llevar un control del acceso a los usuarios, cuenta con un sistema para la creación de una cuenta de usuario, inicio de sesión y un restablecedor de contraseña en caso de olvidarla, para acceder a la sección de productos el usuario deberá estar logeado.

## Tecnologías usadas

- Python versión 3.8.5
- Framework Django versión 4.2.5
- Bootstrap versión 5.3
- CSS
- HTML5

## Instalación

1. Clona este repositorio: `https://github.com/AndresSilverall/User-authentication-system.git`
2. Navega a la carpeta del proyecto: `cd User-authentication-system`
3. Ejecuta un entorno virtual de Python para la ejecución de la App

### Instalar venv en Python

- Instalar desde el gestor de paquetes de Python: `pip install venv`
- Crear un entorno virtual: `python -m venv venv`
- Navegar al entorno virtual creado: `cd venv`
- Luego ingresar a `cd Scripts`
- Presionar `activate` dentro de la carpeta `Scripts` para activar el entorno virtual
- Una vez ya activado el entorno virtual deberá volver a la carpeta raíz del proyecto
- Desde la carpeta raíz del proyecto instalar todas las dependencias de la aplicación con `pip install -r requirements.txt`

4. Ejecuta el servidor de desarrollo: `python manage.py runserver`
5. Abre tu navegador y ve a: `http://127.0.0.1:8000/`

## App en ejecución

![App en ejecución](assets/app.gif)
