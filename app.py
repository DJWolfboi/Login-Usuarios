from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'clave_super_secreta'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Simulación de base de datos en memoria
usuarios = {
    'usuario1': {
        'nombre': 'usuario1',
        'contraseña': generate_password_hash('password123'),
        'rol': 'admin'
    }
}

class Usuario(UserMixin):
    def __init__(self, nombre):
        self.id = nombre
        self.rol = usuarios[nombre]['rol']

@login_manager.user_loader
def load_user(nombre):
    if nombre in usuarios:
        return Usuario(nombre)
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']
        if nombre in usuarios and check_password_hash(usuarios[nombre]['contraseña'], contraseña):
            usuario = Usuario(nombre)
            login_user(usuario)
            flash('Inicio de sesión exitoso.')
            return redirect(url_for('panel'))
        else:
            flash('Credenciales inválidas.', 'error')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada exitosamente.')
    return redirect(url_for('login'))

@app.route('/panel')
@login_required
def panel():
    return render_template('panel.html', usuario=current_user.id, rol=current_user.rol)

if __name__ == '__main__':
    app.run(debug=True)