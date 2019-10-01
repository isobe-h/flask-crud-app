from flask_blog import app, db
from flask import request, redirect, url_for, render_template, flash, session
from flask_blog.models.entries import Entry
from flask_blog.views.views import login_required

@login_required
@app.route('/')
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template("/entries/index.html", entries=entries)

@login_required
@app.route('/entries/<int:id>', methods=["GET"])
def show_entry(id):
    entry = Entry.query.get(id)
    return render_template('entries/show.html',entry=entry)

@login_required
@app.route('/entries/<int:id>/edit', methods=["GET"])
def edit_entry(id):
    entry = Entry.query.get(id)
    return render_template('entries/edit.html',entry=entry)

@login_required
@app.route("/entries/new", methods=["GET"])
def new_entry():
    return render_template("/entries/new.html")

@login_required
@app.route("/entries", methods=["POST"])
def add_entry():
    entry = Entry(
        title=request.form["title"],
        text=request.form["text"]
    )
    db.session.add(entry)
    db.session.commit()
    flash("新しい記事が作成されました")
    return redirect(url_for("show_entries"))


@app.route("/entries/<int:id>/delete", methods=["POST"])
@login_required
def delete_entry(id):
    entry = Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    flash("記事が削除されました")
    return redirect(url_for('show_entries'))

@login_required
@app.route("/entries/<int:id>/update", methods=["POST"])
def update_entry(id):
    entry = Entry.query.get(id)
    entry.title = request.form["title"]
    entry.text = request.form["text"]
    db.session.merge(entry)
    db.session.commit()
    flash("記事が更新されました")
    return redirect(url_for('show_entries'))