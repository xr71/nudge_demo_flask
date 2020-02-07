from flask import Flask
from flask import render_template
from flask import jsonify
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/aboutus')
def aboutus():

    return ''


@app.route('/contactus')
def contactus():

    return ''


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)