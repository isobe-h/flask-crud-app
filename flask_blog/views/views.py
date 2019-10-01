# flask_ blog/ views. py
from flask_blog import app
from flask import request, redirect, url_for, render_template, flash, session


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != app.config["USERNAME"]:
            flash("ユーザ名が異なる")
        elif request.form["password"] != app.config["PASSWORD"]:
            flash("パスワードが異なる")
        else:
            session["logged_in"] = True
            flash("ログインしました")
            return redirect(url_for("show_entries"))
    return render_template("login.html")



@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("ログアウトしました")
    return redirect(url_for("show_entries"))
