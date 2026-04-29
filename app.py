from flask import Flask, render_template, request, redirect
app = Flask(__name__)
skills = [] # 입력한 기술명들 서버 메모리에 임시로 저장해두는 리스트.

@app.route("/")
def index():
    return render_template("index.html", skills=skills)

@app.route("/add", methods=["POST"]) 
def add():
    skill = request.form.get("skill") # HTML의 inputname s에 사용자가 입력한 글자내용 가져옴

    if skill:
        skills.append(skill) # 가져온 글자를 skills리스트에 하나씩추가

    return redirect("/") # 데이터추가끝나고 다시 메인페이지로 화면전환
app.run(debug=True)