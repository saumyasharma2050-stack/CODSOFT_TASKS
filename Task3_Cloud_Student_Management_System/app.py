from flask import Flask, render_template, redirect, url_for
from config import Config
from extensions import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from models import Student, Course, Attendance, Grade
from forms import StudentForm, CourseForm, AttendanceForm, GradeForm


# =====================================
# HOME
# =====================================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")

# =====================================
# DASHBOARD
# =====================================

@app.route("/dashboard")
def dashboard():

    total_students = Student.query.count()
    total_courses = Course.query.count()
    total_attendance = Attendance.query.count()
    total_grades = Grade.query.count()

    return render_template(
        "dashboard.html",
        total_students=total_students,
        total_courses=total_courses,
        total_attendance=total_attendance,
        total_grades=total_grades
    )
# =====================================
# STUDENT ROUTES
# =====================================

@app.route("/students")
def students():
    students = Student.query.all()
    return render_template("students.html", students=students)


@app.route("/add_student", methods=["GET", "POST"])
def add_student():

    form = StudentForm()

    if form.validate_on_submit():

        student = Student(
            name=form.name.data,
            roll_number=form.roll_number.data,
            email=form.email.data,
            course=form.course.data,
            semester=form.semester.data
        )

        db.session.add(student)
        db.session.commit()

        return redirect(url_for("students"))

    return render_template("add_student.html", form=form)


@app.route("/edit_student/<int:id>", methods=["GET", "POST"])
def edit_student(id):

    student = Student.query.get_or_404(id)

    form = StudentForm(obj=student)

    if form.validate_on_submit():

        student.name = form.name.data
        student.roll_number = form.roll_number.data
        student.email = form.email.data
        student.course = form.course.data
        student.semester = form.semester.data

        db.session.commit()

        return redirect(url_for("students"))

    return render_template("edit_student.html", form=form)


@app.route("/delete_student/<int:id>")
def delete_student(id):

    student = Student.query.get_or_404(id)

    db.session.delete(student)
    db.session.commit()

    return redirect(url_for("students"))


# =====================================
# COURSE ROUTES
# =====================================

@app.route("/courses")
def courses():

    courses = Course.query.all()

    return render_template("courses.html", courses=courses)


@app.route("/add_course", methods=["GET", "POST"])
def add_course():

    form = CourseForm()

    if form.validate_on_submit():

        course = Course(
            course_name=form.course_name.data,
            course_code=form.course_code.data
        )

        db.session.add(course)
        db.session.commit()

        return redirect(url_for("courses"))

    return render_template("add_course.html", form=form)


@app.route("/edit_course/<int:id>", methods=["GET", "POST"])
def edit_course(id):

    course = Course.query.get_or_404(id)

    form = CourseForm(obj=course)

    if form.validate_on_submit():

        course.course_name = form.course_name.data
        course.course_code = form.course_code.data

        db.session.commit()

        return redirect(url_for("courses"))

    return render_template("edit_course.html", form=form)


@app.route("/delete_course/<int:id>")
def delete_course(id):

    course = Course.query.get_or_404(id)

    db.session.delete(course)
    db.session.commit()

    return redirect(url_for("courses"))


# =====================================
# ATTENDANCE ROUTES
# =====================================

@app.route("/attendance")
def attendance():

    attendance_records = Attendance.query.all()

    return render_template(
        "attendance.html",
        attendance_records=attendance_records
    )


@app.route("/add_attendance", methods=["GET", "POST"])
def add_attendance():

    form = AttendanceForm()

    if form.validate_on_submit():

        attendance = Attendance(
            student_id=form.student_id.data,
            attendance_percentage=form.attendance_percentage.data
        )

        db.session.add(attendance)
        db.session.commit()

        return redirect(url_for("attendance"))

    return render_template("add_attendance.html", form=form)


@app.route("/edit_attendance/<int:id>", methods=["GET", "POST"])
def edit_attendance(id):

    attendance = Attendance.query.get_or_404(id)

    form = AttendanceForm(obj=attendance)

    if form.validate_on_submit():

        attendance.student_id = form.student_id.data
        attendance.attendance_percentage = form.attendance_percentage.data

        db.session.commit()

        return redirect(url_for("attendance"))

    return render_template("edit_attendance.html", form=form)


@app.route("/delete_attendance/<int:id>")
def delete_attendance(id):

    attendance = Attendance.query.get_or_404(id)

    db.session.delete(attendance)
    db.session.commit()

    return redirect(url_for("attendance"))


# =====================================
# GRADE ROUTES
# =====================================

@app.route("/grades")
def grades():

    grades = Grade.query.all()

    return render_template("grades.html", grades=grades)


@app.route("/add_grade", methods=["GET", "POST"])
def add_grade():

    form = GradeForm()

    if form.validate_on_submit():

        grade = Grade(
            student_id=form.student_id.data,
            subject=form.subject.data,
            grade=form.grade.data
        )

        db.session.add(grade)
        db.session.commit()

        return redirect(url_for("grades"))

    return render_template("add_grade.html", form=form)


@app.route("/edit_grade/<int:id>", methods=["GET", "POST"])
def edit_grade(id):

    grade = Grade.query.get_or_404(id)

    form = GradeForm(obj=grade)

    if form.validate_on_submit():

        grade.student_id = form.student_id.data
        grade.subject = form.subject.data
        grade.grade = form.grade.data

        db.session.commit()

        return redirect(url_for("grades"))

    return render_template("edit_grade.html", form=form)


@app.route("/delete_grade/<int:id>")
def delete_grade(id):

    grade = Grade.query.get_or_404(id)

    db.session.delete(grade)
    db.session.commit()

    return redirect(url_for("grades"))


# =====================================
# DATABASE
# =====================================

with app.app_context():
    db.create_all()


# =====================================
# RUN APPLICATION
# =====================================

if __name__ == "__main__":
    app.run(debug=True)