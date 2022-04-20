from flask_app import app
from flask_app.controllers import surveys_controller

# From original assignment dojo_survey - not needed for this assignment
# from flask import Flask, render_template, request, redirect, session

# app = Flask(__name__)
# app.secret_key = "keep it secret and safe"

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/process', methods=['POST'])
# def form():

#     print(request.form)

#     session['name'] = request.form['name']
#     session['dojo_location'] = request.form['dojo_location']
#     session['favorite_language'] = request.form['favorite_language']
#     session['comments'] = request.form['comments']
#     return redirect('/result')

# @app.route('/result')
# def result():

#     print(session)

#     return render_template(
#         "display.html",
#         name = session['name'],
#         dojo_location = session['dojo_location'],
#         favorite_language = session['favorite_language'],
#         comments = session['comments']
#     )

if __name__ == '__main__':
    app.run(debug=True, port = 5000)