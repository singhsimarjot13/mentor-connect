from flask import Flask, abort, render_template, redirect, url_for, flash,request
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user,login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from werkzeug.security import generate_password_hash, check_password_hash
import  sqlalchemy.exc
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


login_=LoginManager()
app = Flask(__name__)
app.config['SECRET_KEY'] = "HELLO"
login_.init_app(app)
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///yo.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

@login_.user_loader
def load_user(user_id):
    return db.get_or_404(User,user_id)



# User model for both mentors and students
class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password=db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(10), nullable=False)  # 'mentor' or 'student'
    bio = db.Column(db.Text)
    skills = db.Column(db.String(200))  # For mentors
    interests = db.Column(db.String(200))  # For students
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.name}, {self.role}>'

# Mentor-Student connection model
class MentorStudent(db.Model):
    __tablename__ = 'mentor_student'
    id = db.Column(db.Integer, primary_key=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    connection_date = db.Column(db.DateTime, default=datetime.utcnow)

    mentor = db.relationship('User', foreign_keys=[mentor_id], backref='mentor_connections')
    student = db.relationship('User', foreign_keys=[student_id], backref='student_connections')

    def __repr__(self):
        return f'<Mentor-Student {self.mentor_id} -> {self.student_id}>'

# Session table to log sessions between mentor and student
class Session(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    session_date = db.Column(db.DateTime, default=datetime.utcnow)
    topic = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.Text)

    mentor = db.relationship('User', foreign_keys=[mentor_id], backref='mentor_sessions')
    student = db.relationship('User', foreign_keys=[student_id], backref='student_sessions')

    def __repr__(self):
        return f'<Session {self.topic} on {self.session_date}>'

# Schedule table for booking time slots with mentors
class Schedule(db.Model):
    __tablename__ = 'schedules'
    id = db.Column(db.Integer, primary_key=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    scheduled_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'confirmed', 'completed'
    notes = db.Column(db.Text)

    mentor = db.relationship('User', foreign_keys=[mentor_id], backref='mentor_schedules')
    student = db.relationship('User', foreign_keys=[student_id], backref='student_schedules')

    def __repr__(self):
        return f'<Schedule Mentor: {self.mentor_id}, Student: {self.student_id}, Time: {self.scheduled_time}, Status: {self.status}>'
with app.app_context():
    db.create_all()

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        confirm_password=request.form.get('confirm')
        role=request.form.get("role")
        if confirm_password==password:
            result = db.session.execute(db.select(User).where(User.email == email))
            # Note, email in db is unique so will only have one result.
            user = result.scalar()
            if user:
                # User already exists
                flash("You've already signed up with that email, log in instead!")
                return redirect(url_for('login'))
            password=generate_password_hash(password,method='pbkdf2:sha256',salt_length=8)
            result=User(
                email=email,
                password=password,
                role=role
            )
            try:
             db.session.add(result)
             db.session.commit()
            except sqlalchemy.exc.IntegrityError as e:
                print("IntegrityError occurred:", e)
            return redirect(url_for('login'))
        else:
         return render_template("signup.html",current_user=current_user)
    return render_template("signup.html", current_user=current_user)


# TODO: Retrieve a user from the database based on their email.
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        check=db.session.execute(db.select(User).where(User.email==email)).scalar()
        if check:
            if check_password_hash(check.password,password):
                login_user(check)
                return redirect(url_for('register'))
            else:
                flash('wrong password!please try again!')
        else:
            flash('wrong email!please try again.')
    return render_template("login.html", current_user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.html'))
if __name__=="__main__":
    app.run(debug=True,port=5000)