# Proyecto Flask: Sistema de Registro y Autenticación de Usuarios

Este proyecto es una aplicación web básica desarrollada con **Flask**, que incluye formularios con **WTForms**, validaciones personalizadas, y un sistema de autenticación usando **Flask-Login**. Fue creado como parte del curso de desarrollo web con Python.

## 🔧 Funcionalidades principales

- Registro de usuarios con validaciones:
  - Nombre obligatorio (mínimo 3 caracteres)
  - Correo válido
  - Contraseña segura (mínimo 6 caracteres)
- Inicio de sesión con autenticación segura
- Uso de contraseñas encriptadas con `werkzeug.security`
- Gestión de sesiones con Flask-Login
- Rutas protegidas para usuarios autenticados
- Estructura de templates con Jinja2

## 📁 Estructura del proyecto

```plaintext
mi_app_flask/
├── app.py            # Código Python con la lógica de Flask
├── templates/        # Plantillas HTML
│   ├── index.html    # Página de inicio
│   ├── login.html  # Página de Iniciar Sesion
│   └── panel.html  # Página despues de Iniciar sesion
└── requirements.txt  # Dependencias del proyecto
```

## 🚀 Cómo ejecutar el proyecto

1. Clona el repositorio:
   ```plaintext
   git clone https://github.com/DJWolfboi/Login-Usuarios.git
   ```
 2. Crea un entorno virtual e instálalo:
```plaintext
python -m venv venv
source venv/bin/activate  # En Windows usa venv\Scripts\activate
```
```plaintext
pip install -r requirements.txt
```

Ejecuta la aplicación:
```plaintext
python app.py
```
Abre tu navegador en http://localhost:5000


🔒 Consideraciones de seguridad
Las contraseñas se almacenan en formato hash.

Las rutas están protegidas para evitar acceso no autorizado.

No se guarda información sensible en texto plano.

📚 Tecnologías utilizadas
Python 3

Flask

Flask-Login

WTForms

Jinja2

Werkzeug Security
