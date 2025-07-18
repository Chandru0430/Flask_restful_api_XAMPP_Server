from flask import Flask, render_template, request, flash, redirect, url_for
import db  # Assuming db.py contains the database functions
from db import get_connection, insert_contact
 
app = Flask(__name__, template_folder='templates')
app.secret_key = 'your_secret_key'  # Needed for flashing messages
 
@app.route('/')
def home():
    return render_template('home.html')
 
@app.route('/about')
def about():
    return render_template('about.html')
 
@app.route('/services')
def services():
    return render_template('services.html')
 
@app.route('/technology')
def technology():
    return render_template('technology.html')
 
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        mobile_number = request.form.get('mobile_number')
        location = request.form.get('location')
        message = request.form.get('message')
        db.insert_contact(name, email, mobile_number, location, message)
        flash('Thank you for contacting us!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')
 
if __name__ == '__main__':
    app.run(debug=True)
