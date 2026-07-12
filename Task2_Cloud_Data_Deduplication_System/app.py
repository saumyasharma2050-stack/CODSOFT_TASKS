from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
import pandas as pd

# ----------------------------------------------------
# Create Flask App
# ----------------------------------------------------
app = Flask(__name__)
app.config.from_object(Config)

# ----------------------------------------------------
# Initialize Database
# ----------------------------------------------------
db = SQLAlchemy(app)

# ----------------------------------------------------
# Database Model
# ----------------------------------------------------
class Record(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<Record {self.name}>"

# ----------------------------------------------------
# Home Page
# ----------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ----------------------------------------------------
# Login Page
# ----------------------------------------------------
@app.route("/login")
def login():
    return render_template("login.html")


# ----------------------------------------------------
# Register Page
# ----------------------------------------------------
@app.route("/register")
def register():
    return render_template("register.html")


# ----------------------------------------------------
# Dashboard
# ----------------------------------------------------

@app.route("/dashboard")
def dashboard():

    # Total number of records
    total_records = Record.query.count()

    # Count of unique email addresses
    unique_emails = db.session.query(Record.email).distinct().count()

    # Last uploaded record
    last_record = Record.query.order_by(Record.id.desc()).first()

    return render_template(
        "dashboard.html",
        total_records=total_records,
        unique_emails=unique_emails,
        last_record=last_record
    )

# ----------------------------------------------------
# Upload CSV
# ----------------------------------------------------
@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        uploaded_file = request.files.get("file")

        if uploaded_file and uploaded_file.filename != "":

            try:

                data = pd.read_csv(uploaded_file)

                added = 0
                skipped = 0

                for index, row in data.iterrows():

                    name = str(row["Name"]).strip()
                    email = str(row["Email"]).strip().lower()

                    existing = Record.query.filter_by(email=email).first()

                    if existing:
                        skipped += 1
                        continue

                    new_record = Record(
                        name=name,
                        email=email
                    )

                    db.session.add(new_record)
                    added += 1

                db.session.commit()

                return render_template(
                    "upload_result.html",
                    added=added,
                    skipped=skipped
                )

            except Exception as e:

                return f"""
                <h2>Error While Uploading CSV</h2>
                <p>{e}</p>
                <br>
                <a href="/upload">Go Back</a>
                """

    return render_template("upload.html")


# ----------------------------------------------------
# View Records + Search
# ----------------------------------------------------
@app.route("/records")
def records():

    search = request.args.get("search", "").strip()

    if search:

        all_records = Record.query.filter(

            (Record.name.contains(search)) |

            (Record.email.contains(search))

        ).order_by(Record.id).all()

    else:

        all_records = Record.query.order_by(Record.id).all()

    return render_template(

        "records.html",

        records=all_records,

        search=search

    )


# ----------------------------------------------------
# Delete Record
# ----------------------------------------------------
@app.route("/delete/<int:id>")
def delete(id):

    record = Record.query.get_or_404(id)

    db.session.delete(record)

    db.session.commit()

    return redirect(url_for("records"))


# ----------------------------------------------------
# Main Function
# ----------------------------------------------------
if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)