from flask import Flask, render_template, request, redirect, url_for

from app import app

users = []


@app.route('/', methods=['GET', 'POST'])
def user_form():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        hobby = request.form['hobby']
        age = request.form['age']
        users.append({'name': name, 'city': city, 'hobby': hobby, 'age': age})
        return redirect(url_for("user_form"))
    return render_template('users.html', users=users)
