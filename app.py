from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars, time

app = Flask(__name__)
app.config['MONGO_URI']= "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

info = None
if info == None:
    info=scrape_mars.scrape()


@app.route('/')
def index():
    
    return render_template('index.html',fi=app.info['featured image'], h1=app.info['hemispheres'][0],\
        h2=app.info['hemispheres'][1],h3=app.info['hemispheres'][2],h4=app.info['hemispheres'][3],\
            table=app.info['table'],news=app.info['news_p'],headline=app.info['news_title'])


@app.route('/scrape')
def get_info():
    app.info =scrape_mars.scrape()
    time.sleep(3)
    return redirect('..', code=301)

@app.route('/json')
def display_info():
    return info
 
if __name__ == "__main__":
    app.run(host= 'localhost',port =5000,debug=True)