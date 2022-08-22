from flask import Flask, render_template, request, redirect, url_for, flash, session
from database.config import mysql
from werkzeug.security import check_password_hash, generate_password_hash
from models.users import User

#login
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        #cek data username
        user = User.query.filter_by(email=email).first()
        akun = user.fetchone()
        if akun is None:
            flash('Login Gagal, Cek Username Anda','danger')
        elif not check_password_hash(akun[3], password):
            flash('Login gagal, Cek Password Anda', 'danger')
        else:
            session['loggedin'] = True
            session['username'] = akun[4]
            session['level'] = akun[5]
            if session['level'] == 'ADMIN':
                flash('Login Admin Successfully', 'success')
                return redirect(url_for('persons'))
            elif session['level'] == 'EMPLOYEE':
                flash('Login Employee Successfully', 'success')
                return redirect(url_for('ajax'))
            else:
                return redirect(url_for('data'))
    return render_template('auth/login.html')
