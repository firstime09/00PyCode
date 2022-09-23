import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

cur.execute('''CREATE TABLE tbuku( id CHAR(4) NOT NULL PRIMARY KEY,
judul VARCHAR(40), penulis VARCHAR(25), penerbit VARCHAR(30))''')

cur.execute('INSERT INTO tbuku VALUES(?,?,?,?)',
			('A01', 'Pemrograman Python', 'Blessy Jeniffer', 'Vanda Press'))

cur.execute('INSERT INTO tbuku VALUES(?,?,?,?)',
			('A02', 'Pemrograman Python Flask', 'Brino Ferdinand', 'Vanda Press'))
			
con.commit()
cur.close()
con.close()
