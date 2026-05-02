from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_KEY')
Bootstrap5(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/origin', methods=['GET'])
def origin():
    return render_template('origin.html')


@app.route('/spouse', methods=['GET'])
def spouse():
    return render_template('spouse.html')


@app.route('/child_parent', methods=['GET'])
def child_parent():
    return render_template('child_parent.html')


@app.route('/parent_child', methods=['GET'])
def parent_child():
    return render_template('parent_child.html')


@app.route('/sibling', methods=['GET'])
def sibling():
    return render_template('sibling.html')


@app.route('/summary', methods=['GET'])
def summary():
    return render_template('summary.html')


if __name__ == "__main__":
    app.run(debug=True)
