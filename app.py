from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars, time

app = Flask(__name__)
app.config['MONGO_URI']= "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

info = None



@app.route('/')
def index():
    global info
    if info == None:
        info=scrape_mars.scrape()
    return render_template('index.html',fi=info['featured image'], h1=info['hemispheres'][0],\
        h2=info['hemispheres'][1],h3=info['hemispheres'][2],h4=info['hemispheres'][3],\
            table=info['table'],news=info['news_p'],headline=info['news_title'])


@app.route('/scrape')
def get_info():
    global info
    info = scrape_mars.scrape()
    for i in range(30):
        time.sleep(1)
        if i==20:
            return redirect('localhost:5000', code=301)
    
#return json info for debugging
@app.route('/json')
def display_info():
    global info
    return info
 
if __name__ == "__main__":
    app.run(host= 'localhost',port =5000,debug=True)