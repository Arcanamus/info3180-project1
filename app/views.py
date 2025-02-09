"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, flash, request, redirect, url_for, send_from_directory
from .forms import PropertyForm
from app.models import PropertyProfile
from werkzeug.utils import secure_filename


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Jevon Forrest")

@app.route('/properties/create', methods = ["GET", "POST"])
def create_new_property():
    """Render form and create new properties."""
    form = PropertyForm()
    if request.method == 'POST' and form.validate_on_submit():
        title = request.form['title']
        bedrooms = request.form['bedrooms']
        bathrooms = request.form['bathrooms']
        location = request.form['location']
        price = request.form['price']
        type = request.form['type']
        description = request.form['description']
        filename = save_image(form.photo.data)
        property = PropertyProfile(title, description, bedrooms, bathrooms, price, type, location, filename)
        db.session.add(property)
        db.session.commit()
        flash('Property added!', 'success')
        return redirect(url_for('view_properties'))
    return render_template('new_property.html', form=form)


@app.route('/properties', methods=["GET"])
def view_properties():
    """Render list of properties."""
    properties = db.session.query(PropertyProfile).all()
    return render_template('properties.html', properties=properties)

@app.route('/property/<propertyid>', methods=["GET"])
def show_property(propertyid):
    """Render property search by id."""
    prop_search = db.session.query(PropertyProfile).filter(PropertyProfile.id == propertyid).first()
    return render_template('property.html', prop_search=prop_search)

@app.route('/get_image/<filename>')
def get_image(filename):
    """Fetches images to be displayed"""
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)

###
# The functions below should be applicable to all Flask apps.
###

def save_image(photo):
    filename = secure_filename(photo.filename)
    photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return filename

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

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
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
