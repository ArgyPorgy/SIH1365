# from flask import Flask, render_template, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import InputRequired, Length, ValidationError
# from flask_bcrypt import Bcrypt

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class Org(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orgname = db.Column(db.String(20), nullable=False, unique=True)
    orgtype = db.Column(db.String(80), nullable=False)
    metawallet = db.Column(db.String(80), nullable=False)

class OrgForm(FlaskForm):
    orgname = StringField('Organization Name', validators=[
                         InputRequired(), Length(min=4, max=20)])
    orgtype = StringField('Organization Type', validators=[
                         InputRequired(), Length(min=4, max=80)])
    metawallet = StringField('Metamask Wallet ID', validators=[
                             InputRequired(), Length(min=4, max=80)])
    submit = SubmitField('Register') 

@app.route('/', methods=['GET', 'POST'])
def register():
    form = OrgForm()
    if form.validate_on_submit():
        hashed_wallet = bcrypt.generate_password_hash(
            form.metawallet.data).decode('utf-8')
        new_org = Org(
            orgname=form.orgname.data, orgtype=form.orgtype.data, metawallet=hashed_wallet)
        db.session.add(new_org)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return "Registration successful!"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()   
        app.run(debug=True,port = 8000)

