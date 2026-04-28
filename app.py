from flask import Flask, render_template, request, redirect
app = Flask(__name__)
skills = []

@app.route("/")
def index():
    return render_template("index.html", skills=skills)

@app.route("/add", methods=["POST"])
def add():
    skill = request.form.get("skill")

    if skill:
        skills.append(skill)

    return redirect("/")
app.run(debug=True)