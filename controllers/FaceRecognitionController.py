from database.config import mycursor
from flask import Flask, render_template, redirect, url_for, flash, session

def person():
    mycursor.execute("select prs_nbr, prs_name, prs_skill, prs_active, prs_added from prs_mstr")
    data = mycursor.fetchall()
    return render_template('admin/pages/face_recognition/person.html', data=data)
