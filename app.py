from flask import Flask, render_template, request
from send_email import send_email
# import sys
# import logging

app = Flask(__name__)

# Set "homepage" to index.html

@app.route('/')
def index():
    return render_template('index.html')

# Save e-mail to database and send to next page

@app.route('/next', methods=['POST'])
def next():
    if request.method == 'POST':
        name = request.form['Name']
        email = request.form['Email']
        message = request.form['Message']
        send_email(name, email, message)
        return render_template('next.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
