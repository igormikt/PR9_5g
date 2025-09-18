from flask import render_template, request, redirect, url_for
from app import app

users = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get('name')
        age = request.form.get('age')
        city = request.form.get('city')
        hobby = request.form.get('hobby')

        # Проверка на заполнение обязательных полей
        if name and age and city and hobby:
            user_data = {
                'name': name,
                'age': age,
                'city': city,
                'hobby': hobby
            }
            users.append(user_data)

    return render_template('form.html', users=users)
