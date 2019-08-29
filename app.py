from flask import Flask, render_template, request, url_for,session,flash,redirect
import os
from model import get_post,create_post,create_user,get_user


app = Flask(__name__)
app.config['UPLOAD_FOLDER']='static'
app.secret_key='hello'

def rev_uniq(a):
	i=[]
	k=[]
	for x in a:
		if x not in i:
			i.append(x)
	for j in range(len(i)):
		k.append(i.pop())
	return k

def validate(a,b):
	email=0
	password=0
	name=0
	for i in b:
		if a[0]==i[1]:
			email=email+1
		if a[1]==i[2]:
			password=password+1
	if email==1 and password==1:
		return True			

def getname(a,b):
	for i in b:
		if a[0]==i[1]:
			name=i[0]
	return name		

@app.route('/')
def home():
	return render_template('welcome.html')

@app.route('/register',methods=['POST'])
def register():
	if request.method=='POST':
		name=request.form.get('name')
		email=request.form.get('email')
		password=request.form.get('password')
		create_user(name,email,password)
	flash('login to access your account')	
	return redirect('/')


@app.route('/login',methods=['POST'])
def login():
	if request.method=='POST':
		email=request.form.get('email')
		password=request.form.get('password')
		l=[email,password]
		no_user=get_user()
	if validate(l,no_user):
		name=getname(l,no_user)
		info=[email,name]
		return redirect(url_for('user',info=info))
	else:
		flash('please enter correct username and password')
		return redirect('/')


@app.route('/user/<info>')		
def user(info):
	return render_template('upload.html',info=info) 

@app.route('/timeline',methods=['POST'])
def timeline():
	if request.method=='POST':
		file=request.files['file']
		full_filename = os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
		file.save(full_filename)
		create_post(full_filename)
	db_image_data=get_post()	
	image_data=rev_uniq(db_image_data)
	return render_template('index.html',user_image=image_data)