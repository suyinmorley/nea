

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        f = open("users.txt", "w")
        f.write(request.form['pw'])
        f.close()
    return render_template("signup.html")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        pw = request.form['pw']
        f = open("users.txt", "r")
        stored_pw = f.read()
        f.close()
        if pw == stored_pw:
            return "Correct password!"
        else:
            return "Incorrect password!"
    return render_template("index.html")
