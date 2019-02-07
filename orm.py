from flask import Flask, render_template


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog2.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

db.init_app(app)

class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String, nullable = False)
    content = db.Column(db.String, nullable =False)
    author = db.Column(db.String, nullable =False)
    created_at = db.Column(db.String, nullable =False)
    
db.create_all()

@app.route("/")
def index():
    return render_template("index.html")