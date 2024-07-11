from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import os
import MySQLdb.cursors
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' 
app.config['MYSQL_DB'] = 'crud_peliculas'

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mysql = MySQL(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM movies")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', movies=data)

@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        titulo = request.form['titulo']
        director = request.form['director']
        anio = request.form['anio']
        sinopsis = request.form['sinopsis']

        if 'portada' in request.files:
            file = request.files['portada']

            if file.filename == '':
                flash('No se seleccionó ningún archivo.')
                return redirect(request.url)
            
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                portada_url = url_for('static', filename=f'uploads/{filename}')
            else:
                flash('La extensión del archivo no está permitida.')
                return redirect(request.url)
        else:
            portada_url = None
        
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO movies (titulo, director, anio, portada, sinopsis) VALUES (%s, %s, %s, %s, %s)",
                       (titulo, director, anio, portada_url, sinopsis))
        mysql.connection.commit()
        cursor.close()
        flash('Película agregada correctamente.')
        return redirect(url_for('index'))
    
    return render_template('add_movie.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_movie(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM movies WHERE id = %s", (id,))
    movie = cursor.fetchone()
    cursor.close()

    if request.method == 'POST':
        titulo = request.form['titulo']
        director = request.form['director']
        anio = request.form['anio']
        sinopsis = request.form['sinopsis']

        if 'portada' in request.files:
            file = request.files['portada']

            if file.filename != '':
                if allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    portada_url = url_for('static', filename=f'uploads/{filename}')
                else:
                    flash('La extensión del archivo no está permitida.')
                    return redirect(request.url)
            else:
                portada_url = movie['portada']
        else:
            portada_url = movie['portada']

        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE movies
            SET titulo = %s, director = %s, anio = %s, portada = %s, sinopsis = %s
            WHERE id = %s
        """, (titulo, director, anio, portada_url, sinopsis, id))
        mysql.connection.commit()
        cursor.close()
        flash('Película actualizada correctamente.')
        return redirect(url_for('index'))

    return render_template('edit.html', movie=movie)

@app.route('/delete/<int:id>')
def delete_movie(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM movies WHERE id = %s", (id,))
    mysql.connection.commit()
    cursor.close()
    flash('Película eliminada correctamente.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
