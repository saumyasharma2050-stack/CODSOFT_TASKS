from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Email


class StudentForm(FlaskForm):
    name = StringField("Student Name", validators=[DataRequired()])
    roll_number = StringField("Roll Number", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    course = StringField("Course", validators=[DataRequired()])
    semester = StringField("Semester", validators=[DataRequired()])
    submit = SubmitField("Save Student")


class CourseForm(FlaskForm):
    course_name = StringField("Course Name", validators=[DataRequired()])
    course_code = StringField("Course Code", validators=[DataRequired()])
    submit = SubmitField("Save Course")


class AttendanceForm(FlaskForm):
    student_id = StringField("Student ID", validators=[DataRequired()])
    attendance_percentage = FloatField(
        "Attendance Percentage",
        validators=[DataRequired()]
    )
    submit = SubmitField("Save Attendance")


class GradeForm(FlaskForm):
    student_id = StringField("Student ID", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    grade = StringField("Grade", validators=[DataRequired()])
    submit = SubmitField("Save Grade")