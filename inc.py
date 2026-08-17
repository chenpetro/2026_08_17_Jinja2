from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main1.html")

@app.route("/2")
def main2():
    return render_template("main2.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/main1")
def main1():
    return render_template("main1.html")

@app.route("/main2")
def main3():
    return render_template("main2.html")

app.run(debug=True)