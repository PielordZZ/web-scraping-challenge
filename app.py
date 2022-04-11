from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
app.config['MONGO_URI']= "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

info =scrape_mars.scrape()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scrape')
def get_info():
    scrape_mars.scrape()
    return redirect('..', code=301)

@app.route('/json')
def display_info():
    return info()

if __name__ == "__main__":
    app.run(host= 'localhost',port =5000,debug=True)