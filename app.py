from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("UPDATE users SET password = ? WHERE username = ?", (request.form['pw'], request.form['username']))
        con.commit()
        con.close()
        return "Password changed successfully!"
    return render_template("admin.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (request.form['username'], request.form['pw']))
        con.commit()
        con.close()
        return "User created successfully!"
    return render_template("signup.html")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        pw = request.form['pw']
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (request.form['username'], request.form['pw']))
        result = cur.fetchone()
        if result:
            return "Correct password!"
        else:
            return "Incorrect password!"
    return render_template("index.html")
