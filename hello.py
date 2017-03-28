"""
Flask app toolbox code
"""

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']

        if len(firstname) > 0 and len(lastname) > 0:
            return render_template('profile.html', firstname = firstname, lastname = lastname)
        else:
            return render_template('error.html')


if __name__ == '__main__':
    app.run()
