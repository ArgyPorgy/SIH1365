
from flask import Flask, render_template, redirect, url_for,request
from flask_sqlalchemy import SQLAlchemy
import sqlite3
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import InputRequired, Length
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# class Org(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     orgname = db.Column(db.String(20), nullable=False, unique=True)
#     orgtype = db.Column(db.String(80), nullable=False)
#     metawallet = db.Column(db.String(80), nullable=False)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), nullable=False, unique=True)
#     aadhar = db.Column(db.String(80), nullable=False)
#     metawallet = db.Column(db.String(80), nullable=False)

# class RegistrationForm(FlaskForm):
#     orgname = StringField('Organization Name', validators=[
#                          InputRequired(), Length(min=4, max=20)])
#     orgtype = StringField('Organization Type', validators=[
#                          InputRequired(), Length(min=4, max=80)])
#     org_metawallet = StringField('Metamask Wallet ID', validators=[
#                              InputRequired(), Length(min=4, max=80)])
#     username = StringField('Your Name', validators=[
#                          InputRequired(), Length(min=4, max=20)])
#     aadhar = StringField('Your Aadhar card no.', validators=[
#                          InputRequired(), Length(min=4, max=80)])
#     user_metawallet = StringField('Metamask Wallet ID', validators=[
#                              InputRequired(), Length(min=4, max=80)])
#     password = StringField('Your password', validators=[
#                              InputRequired(), Length(min=4, max=10)])
#     submit = SubmitField('Register')     

# @app.route('/', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user_form = request.form.get('user_form')
#         org_form = request.form.get('org_form')

#         if user_form:
#             user_hashed_wallet = bcrypt.generate_password_hash(
#                 form.user_metawallet.data).decode('utf-8')
#             hashed_password = bcrypt.generate_password_hash(
#                 form.password.data).decode('utf-8')
#             new_user = User(
#                 username=form.username.data, aadhar=form.aadhar.data, user_metawallet=user_hashed_wallet, password=hashed_password)
#             db.session.add(new_user)
#             db.session.commit()

#         elif org_form:
#             org_hashed_wallet = bcrypt.generate_password_hash(
#                 form.org_metawallet.data).decode('utf-8')
#             new_org = Org(
#                 orgname=form.orgname.data, orgtype=form.orgtype.data, org_metawallet=org_hashed_wallet)
#             db.session.add(new_org)
#             db.session.commit()

#         return redirect(url_for('success'))

#     return render_template('index.html', form=form)



# @app.route('/success')
# def success():
#     return "Registration successful!"

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()   
#         app.run(debug=True,port = 8000)


'''
soham's part of DBMS
'''

# considering database has been created already
msg = ""

@app.route("/", methods=['GET', 'POST'])
def index():
    global msg
    if request.method == 'POST':
        try:
            if 'user_form' in request.form:
                user = request.form['username']
                adhr = request.form['aadhar']
                userMW = request.form['user_metawallet']
                pswd = request.form['password']
                cryptPass = bcrypt.generate_password_hash(pswd).decode('utf-8')
                with sqlite3.connect('userData.db') as conn:
                    cur = conn.cursor()
                    cur.execute("INSERT INTO users (username , adhar , walletID, password) VALUES (?, ?,?, ?)",
                                (user, adhr, userMW, cryptPass))
                    conn.commit()
                    print('User registered successfully.')
                    msg = "User Registered Successfully"
                    
            elif 'org_form' in request.form:
                orgname = request.form['orgname']
                orgtype = request.form['orgtype']
                org_metawallet = request.form['org_metawallet']
                with sqlite3.connect('orgData.db') as conn:
                    cur = conn.cursor()
                    cur.execute("INSERT INTO users (orgname , orgtype , org_metawallet) VALUES (?, ?,?)",
                                (orgname, orgtype, org_metawallet))
                    conn.commit()
                print('Official registered successfully.')
                msg = "Official Registered Successfully"

        except Exception as e:
            conn.rollback()
            msg = f"Error: {e}"
        finally:
            conn.close()

    return render_template("index.html", msg=msg)



if __name__ == "__main__":
    app.run(debug=True)


                            

