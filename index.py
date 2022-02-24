from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'relatar'
mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/') 
def home():
    return render_template('home.html')

@app.route('/comenzar')
def comenzar():
    return render_template('comenzar.html')

@app.route('/relato', methods=['POST'])
def relato():
    if request.method == 'POST':
     texto = request.form['texto']
     cur = mysql.connection.cursor()    
     cur.execute ("INSERT INTO escribir (texto) VALUES ('{0}')".format(texto))   
     mysql.connection.commit()
     flash('Historia subida')
    return redirect(url_for('comenzar'))

@app.route('/historias')
def historias():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM escribir')
    data = cur.fetchall()
    return render_template('historias.html', escribir = data)

@app.route('/historia')
def historia():
    return render_template('historia.html')


@app.route('/about')   
def about():
    return render_template('about.html')




if __name__ == '__main__':
    app.run(debug=True)
