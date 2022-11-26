import flask
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
#local computer:
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///officequotes"

#heroku:
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://wyattaddie:Mn3g5WBs_55AFmb@wyattaddie.mysql.pythonanywhere-services.com/wyattaddie$default"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
db_session = db.session

class Person(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    role = db.Column(db.Text())
    gender = db.Column(db.Text())
    approved = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return self.name

class Quote(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.Text())
    episode = db.Column(db.Integer)
    season = db.Column(db.Integer)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    approved = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return self.quote

@app.route('/')
def index():
    people = db_session.query(Person).filter_by(approved=True)
    context = {'name': 'Jim','age': ':)'}
    nums = [{'name': 'Jim','age': ':)'},{'name': 'Dwight','age': ';)'}]
    return render_template('index.html', context=context, people=people)

@app.route('/quotes/<person_id>')
def quotes(person_id):
  quotes = db_session.query(Quote).filter_by(person_id=person_id, approved=True).all()
  person = db_session.query(Person).filter_by(id=person_id, approved=True).first()
  return render_template('quotes.html', quotes=quotes, person=person)

@app.route('/add_person', methods=['GET','POST'])
def add_person():

  if flask.request.method == 'POST':

    new_person = Person(name=flask.request.form.get('name'),role=flask.request.form.get('role'),gender=flask.request.form.get('gender'))
    db_session.add(new_person)
    db_session.commit()
    return flask.redirect('/')
  return render_template('add_user.html')

@app.route('/add_quote', methods=['GET','POST'])
def add_quote():

  if flask.request.method == 'POST':

    new_quote = Quote(quote=flask.request.form.get('quote'),episode=flask.request.form.get('episode'),season=flask.request.form.get('season'),person_id=flask.request.form.get('person_id'))
    db_session.add(new_quote)
    db_session.commit()
    return flask.redirect('/quotes')
  return render_template('add_quote.html')

@app.route('/quotes')
def quote():

  quotes = db_session.query(Quote).filter_by(approved=True)
  person = db_session.query(Person).filter_by(approved=True)
  return render_template('all_quotes.html', quotes=quotes, person=person)
