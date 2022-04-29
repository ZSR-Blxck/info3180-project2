"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, jsonify, send_file
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from flask.helpers import send_from_directory
from flask_cors import CORS,cross_origin
from app.forms import *
from app.models import *
import os, datetime, jwt
from functools import wraps

CORS(app,resources={r"/api": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
###
# Routing for your application.
###

@app.route('/')
@cross_origin(origin='*',headers=['content-type'])
def index():
    return send_file(os.path.join('../dist/', 'index.html'))

@app.route('/api/register', methods=['POST'])
@cross_origin(origin='*',headers=['content-type'])
def register():

    form = RegisterForm()
    
    if request.method=='POST' and form.validate_on_submit():
        
        try:
            name = form.name.data
            uname = form.username.data
            passw = form.password.data
            mail=form.email.data
            location=form.location.data
            bio=form.biography.data
            photo = form.user_photo.data
            date = str(datetime.date.today())
            filename = uname+secure_filename(photo.filename)
                        
            #user = users(username=uname, password=passw, name=name, email=mail, location=location, biography=bio, photo=filename, date_joined=date)
            photo.save(os.path.join("./app",app.config['PROFILE_IMG_UPLOAD_FOLDER'], filename))
            db = connect_db()
            cur=db.cursor()
            cur.execute('insert into user(username,password,name,email,location,biography,photo,date_joined) values (uname, passw, name, email, location, bio, filename, date)' )
            db.session.add(user)
            db.session.commit()
            
            return jsonify(message = "User successfully registered")
            
            
        except Exception as e:
            db.session.rollback()
            print (e)
            return jsonify(errors=["Internal Error"])
    
    return jsonify(errors=form_errors(form))

@app.route('/api/auth/login', methods=["POST"])
@cross_origin(origin='*',headers=['content-type'])
def login():

    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        # change this to actually validate the entire form submission
        # and not just one field
        if form.username.data:
            # Get the username and password values from the form.
            username = form.username.data
            password = form.password.data

            # using your model, query database for a user based on the username
            # and password submitted. Remember you need to compare the password hash.
            # You will need to import the appropriate function to do so.
            # Then store the result of that query to a `user` variable so it can be
            # passed to the login_user() method below.

            user = users.query.filter_by(username=username).first()

            if user is not None and check_password_hash(users.password, password):

                payload = {'user': users.username}
                jwt_token = jwt.encode(payload,app.config['SECRET_KEY'],algorithm = "HS256")
                response = {'message': 'User successfully logged in','token':jwt_token, "user_id": user.id}
            
                return jsonify(response)
            
            return jsonify(errors="Username or password is incorrect")
    
        return jsonify(errors=form_errors(form))

@app.route('/api/auth/logout', methods = ['GET'])
@cross_origin(origin='*',headers=['content-type'])
#@token_authenticate
def logout():
    return jsonify(message= "User successfully logged out.")


@app.route('/api/cars', methods = ['GET','POST'])
@cross_origin(origin='*',headers=['content-type'])
#@token_authenticate
def viewCars():
    if request.method == 'GET':
        getAll = cars.query.all()
        car = []

        for car in getAll:
            user= users.query.filter_by(id=cars.user_id).first()
            carObj = {"id":cars.id, "description":cars.description, "make": cars.make, "colour": cars.colour, "year": cars.year,"transmission":cars.transmission,"car_type":cars.car_type,"price":cars.price,"photo": os.path.join(app.config['PROFILE_IMG_UPLOAD_FOLDER'],cars.photo)}
            cars.append(carObj)

        return jsonify(cars=cars)

    if request.method == 'POST':

        form = CarForm()

        if form.validate_on_submit():

            u_id = form.user_id.data
            description =form.description.data
            make = form.make.data
            colour = form.colour.data
            year = form.year.data
            transmission = form.transmission.data
            car_type = form.car_type.data
            price = form.price.data
            photo = form.photo.data
            
            user = users.query.filter_by(id=u_id).first()

            car = cars(user_id = u_id, description = description, make = make, colour = colour, year = year, transmission= transmission, car_type=car_type, price=price, photo=photo)
            photo.save(os.path.join("./app", app.config['CARS_UPLOAD_FOLDER'],filename))
            db.session.add(car)
            cur=db.cursor()
            cur.execute('insert into cars(user_id, description, make, colour, year, transmission, car_type, price, photo) values (u_id, description, make, colour, year, transmission, car_type, price, photo)' )
            db.session.commit()
            return jsonify(status=201, message="Car Added")
            
            
        print (form.errors.items())
        return jsonify(status=200, errors=form_errors(form))


@app.route('/api/cars/<car_id>/favourite', methods =['GET','POST'])
@cross_origin(origin='*',headers=['content-type'])
#@token_authenticate
def findCar(car_id):
    
    if request.method == 'GET':
        make = Cars.query.filter_by( car_id = car_id).all()
        
        model = Cars.query.filter_by(car_id = car_id).first()
        response = {"status": "ok", "post_data":{"description":cars.description, "make": cars.make, "colour": cars.colour, "year": cars.year,"transmission":cars.transmission,"car_type":cars.car_type,"price":cars.price,"photo": os.path.join(app.config['PROFILE_IMG_UPLOAD_FOLDER'],cars.photo)}}
        
        for favorite in favorites:
            favObj = {"id":favourites.id, "user_id": favourites.user_id, "car_id":favourites.car_id}
            response["post_data"]["favorites"].append(favObj)

        return jsonify(response)
    
    
    if request.method == 'POST':
        
        form = FavForm()
        
        if form.validate_on_submit():
            
            fid = form.user_id.data
            car_id = form.car_id.data
            
            user = users.query.filter_by(id=u_id).first()
            
            fav = favourites(user_id=fid,car_id=car_id,)
            db.session.add(fav)
            db.session.commit()
            return jsonify(status=201, message="New favourite")
            
            
        print (form.errors.items())
        return jsonify(status=200, errors=form_errors(form))

@app.route('/api/cars/<user_id>/favourites', methods =['GET','POST'])
@cross_origin(origin='*',headers=['content-type'])
#@token_authenticate
def findUser(user_id):
    
    if request.method == 'GET':
        user = users.query.filter_by( user_id = user_id).all()
        
        user = users.query.filter_by(user_id = user_id).first()
        response = {"status": "ok", "post_data":{"description":description,"make":make,"colour":colour,"year":year,"transmission":transmission,"car_type":car_type, "price":price, "photo":photo, "user_id":user_id }}
        
        for favourite in favourites:
            favObj = {"id":favourites.id, "user_id": favourites.user_id, "car_id":favourites.car_id}
            response["post_data"]["favorites"].append(favObj)

        return jsonify(response)

    if request.method == 'POST':
        
        form = FavForm()
        
        if form.validate_on_submit():
            
            fid = form.user_id.data
            car_id = form.car_id.data
            
            user = users.query.filter_by(id=u_id).first()
            
            fav = favourites(user_id=fid,car_id=car_id,)
            db.session.add(fav)
            db.session.commit()
            return jsonify(status=201, message="New favourite")
            
            
        print (form.errors.items())
        return jsonify(status=200, errors=form_errors(form))

###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")