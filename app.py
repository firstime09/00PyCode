# from flask import Flask, render_template, request, redirect, url_for
# import pymysql.cursors, os

# application = Flask(__name__)

# conn = cursor = None
# #fungsi koneksi database
# def openDb():
#     global conn, cursor
#     conn = pymysql.connect(host="localhost",user="root",password="",db="db_penjualan" )
#     cursor = conn.cursor()

# #fungsi untuk menutup koneksi
# def closeDb():
#     global conn, cursor
#     cursor.close()
#     conn.close()

# #fungsi view index() untuk menampilkan data dari database
# @application.route('/')
# def index():
#     openDb()
#     container = []
#     sql = "SELECT * FROM barang"
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     for data in results:
#         container.append(data)
#     closeDb()
#     return render_template('index.html', container=container,)

# #fungsi view tambah() untuk membuat form tambah
# @application.route('/tambah', methods=['GET','POST'])
# def tambah():
#     if request.method == 'POST':
#         nama = request.form['nama']
#         harga = request.form['harga']
#         stok = request.form['stok']
#         openDb()
#         sql = "INSERT INTO barang (nama_barang,harga,stok) VALUES (%s, %s, %s)"
#         val = (nama, harga, stok)
#         cursor.execute(sql, val)
#         conn.commit()
#         closeDb()
#         return redirect(url_for('index'))
#     else:
#         return render_template('tambah.html')

# #fungsi view edit() untuk form edit
# @application.route('/edit/<id_barang>', methods=['GET','POST'])
# def edit(id_barang):
#     openDb()
#     cursor.execute('SELECT * FROM barang WHERE id_barang=%s', (id_barang))
#     data = cursor.fetchone()
#     if request.method == 'POST':
#         id_barang = request.form['id_barang']
#         nama = request.form['nama']
#         harga = request.form['harga']
#         stok = request.form['stok']
#         sql = "UPDATE barang SET nama_barang=%s, harga=%s, stok=%s WHERE id_barang=%s"
#         val = (nama, harga, stok, id_barang)
#         cursor.execute(sql, val)
#         conn.commit()
#         closeDb()
#         return redirect(url_for('index'))
#     else:
#         closeDb()
#         return render_template('edit.html', data=data)

# #fungsi untuk menghapus data
# @application.route('/hapus/<id_barang>', methods=['GET','POST'])
# def hapus(id_barang):
#     openDb()
#     cursor.execute('DELETE FROM barang WHERE id_barang=%s', (id_barang,))
#     conn.commit()
#     closeDb()
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     application.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)


# Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.task


# Routes
@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    new_todo = Todo(task=task)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    todo = Todo.query.get_or_404(id)
    todo.task = request.form['task']
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)