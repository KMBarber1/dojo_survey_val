from flask import render_template,request, redirect
from flask_app import app
from flask_app.models.survey import Survey


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create/survey", methods=["POST"])
def create_survey():
    if Survey.is_valid(request.form):
        Survey.save(request.form)
        return redirect("/display")
    return redirect('/')

@app.route("/")
def results():
    return render_template('display.html', survey = Survey.get_last_survey())