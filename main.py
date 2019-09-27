from flask import Flask, render_template, url_for, request,session
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('database.db')
c = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html', name="Home")

app.run(debug=True)