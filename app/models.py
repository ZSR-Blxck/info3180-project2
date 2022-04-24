# Add any model classes for Flask-SQLAlchemy here
from . import db

class cars (db.Model):
	__tablename__ = 'cars'

	id = db.Column(db.Integer,primary_key=True)
	description = db.Column(db.String(255))
	make =  db.Column(db.String(255))
	colour = db.Column(db.String(255))
	year= db.Column(db.String(255))
	transmission = db.Column(db.String(255))
	car_type = db.Column(db.String(255))
	price = db.Column(db.Float)
	photo = db.Column(db.String(255))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self,description,make,colour,year,transmission,car_type,price,photo,user_id):
		self.description =description
		self.make = make
		self.colour = colour
		self.year = year
		self.transmission = transmission
		self.car_type = car_type
		self.price = price
		self.photo = photo
		self.user_id = user_id

class favourites(db.Model):
	__tablename__='favourites'

	id = db.Column(db.Integer,primary_key=True)
	car_id = db.Column(db.Integer)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self,car_id,user_id):
		self.car_id = car_id
		self.user_id = user_id

class users(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	password = db.Column(db.String(25))
	name = db.Column(db.String(80))
	email = db.Column(db.String(80), unique=True)
	location =  db.Column(db.String(255))
	biography = db.Column(db.String(80))
	photo = db.Column(db.String(255))
	date_joined = db.Column(db.DateTime)

	def __init__(self,username,password,name,email,location,biography,photo,date_joined) :
		self.username = username
		self.password = password
		self.name = name 
		self.email = email
		self.location = location
		self.biography = biography
		self.photo = photo
		self.date_joined = date_joined


	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		try:
		    return unicode(self.id)  # python 2 support
		except NameError:
		    return str(self.id)  # python 3 support

	def __repr__(self):
		return '<User %r>' % (self.user_id)
