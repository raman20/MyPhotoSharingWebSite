import sqlite3
from os import path
ROOT = path.dirname(path.relpath((__file__)))
def create_post(filename):
	con=sqlite3.connect(path.join(ROOT,'db.db'))
	cur=con.cursor()
	cur.execute('insert into posts(filename) values(?)',(filename,))
	con.commit()
	con.close()

def get_post():
	con=sqlite3.connect(path.join(ROOT,'db.db'))
	cur=con.cursor()
	cur.execute('select * from posts')
	posts = cur.fetchall()
	return posts	

def create_user(a,b,c):
	con=sqlite3.connect(path.join(ROOT,'db.db'))
	cur=con.cursor()
	cur.execute('insert into user(name,email,password) values(?,?,?)',(a,b,c))
	con.commit()
	con.close()

def get_user():
	con=sqlite3.connect(path.join(ROOT,'db.db'))
	cur=con.cursor()	
	cur.execute('select * from user')
	user=cur.fetchall()
	return user