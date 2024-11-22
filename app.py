from flask import Flask,render_template, redirect, url_for, request
from controllers import controller
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
import os


app = Flask(__name__,template_folder="views")
app.config['SECRET_KEY'] = os.urandom(24)

login_manager = LoginManager(app)

class Usuario(UserMixin):
    def __init__(self, id, username, password, es_admin:bool):
        self.id = id
        self.username = username
        self.password = password
        self.es_admin = es_admin
        
users_db = [
    Usuario(1, 'fabian_1', 'fab_123', True),
    Usuario(2, 'fabian_2', 'fab_123', False),
    Usuario(3, 'fabian_3', 'fab_123', False)
]       
  
  
@login_manager.user_loader
def load_user(user_id):   
    for user in users_db:
        if user.id == int(user_id):
            return user
    return None



@app.route("/")
def index_log():
    return render_template("login.html")

@app.route("/ruta-logueada")
@login_required
def index():
    perros = controller.perros   
    guarderia = controller.guarderia_1
    return render_template("index.html",perros = perros,guarderia=guarderia)

@app.route("/ruta-logueada")
@login_required
def index_noadmin():
    return render_template("index_noadmin.html")


    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':

        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        
        for user in users_db:
            if user.username == username and user.password == password:
                login_user(user)
                if user.es_admin:              
                    
                    return redirect(url_for('index'))
                else:
    
                    return redirect(url_for('index_noadmin'))
            else:
                Flask('Usuario u/o contraseña invalidos!.')
        return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)