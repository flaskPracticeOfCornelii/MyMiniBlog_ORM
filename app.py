from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

db.init_app(app)

class Article(db.Model):
    __tablename__ = "articles"
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer,primary_key = True, autoincrement=True)
    title = db.Column(db.String, nullable = False)
    content = db.Column(db.String, nullable =False)
    author = db.Column(db.String, nullable =False)
    created_at = db.Column(db.String, nullable =False)
    
db.create_all()

##########################################################################################
### ORM #
###########################################################################################
@app.route("/")
def index():
    
    return render_template("index.html")


@app.route("/articles/")
def articles():
    data = Article.query.all()
    
    return render_template("articles.html",data=data)


@app.route("/articles/<int:id>")
def detail(id):
    data = Article.query.get(id)
    
    return render_template("detail.html",data=data)
    

@app.route("/articles/<int:id>/edit")
def edit(id):
    data = Article.query.get(id)
    
    return render_template("edit.html",data=data)


@app.route("/articles/<int:id>/update", methods=["POST"])
def update(id):
    title = request.form.get("title")
    content = request.form.get("content")
    author = request.form.get("author")
    nowtime = str(datetime.now())
    
    data = Article.query.get(id)
    data.title = title
    data.content = content
    data.author = author
    data.created_at = nowtime
    db.session.commit()
    
    return redirect("/articles/{}".format(id))
    

@app.route("/articles/<int:id>/delete")
def delete(id):
    data = Article.query.get(id)
    db.session.delete(data)
    db.session.commit()
    
    return redirect("/articles")


@app.route("/articles/new")
def new():
    
    return render_template("new.html")
    
    
@app.route("/articles/new/create",methods=["POST"])
def create():
    title = request.form.get("title")
    content = request.form.get("content")
    author = request.form.get("author")
    created_at = str(datetime.now())
    
    a = Article(title=title, content=content, author=author, created_at=created_at)
    db.session.add(a)
    db.session.commit()
    
    return redirect("/articles")
