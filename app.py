from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)