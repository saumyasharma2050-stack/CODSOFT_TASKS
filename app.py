from flask import Flask, render_template, request, send_from_directory, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "cloudstorageproject"

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "database", "app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "docx", "txt"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs("database", exist_ok=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        user = User(username=username, email=email, password=password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email, password=password).first()

        if user:
            session["user"] = user.username
            return redirect(url_for("files"))

        return "Invalid Email or Password"

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))


@app.route("/upload", methods=["GET", "POST"])
def upload():

    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        if "file" not in request.files:
            return "No file selected."

        file = request.files["file"]

        if file.filename == "":
            return "Please select a file."

        if not allowed_file(file.filename):
            return "File type not allowed."

        file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))

        return redirect(url_for("files"))

    return render_template("upload.html")


@app.route("/files")
def files():

    if "user" not in session:
        return redirect(url_for("login"))

    files = os.listdir(app.config["UPLOAD_FOLDER"])

    return render_template("files.html", files=files)


@app.route("/download/<filename>")
def download(filename):

    if "user" not in session:
        return redirect(url_for("login"))

    return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)


@app.route("/delete/<filename>")
def delete(filename):

    if "user" not in session:
        return redirect(url_for("login"))

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    if os.path.exists(file_path):
        os.remove(file_path)

    return redirect(url_for("files"))


if __name__ == "__main__":
    app.run(debug=True)