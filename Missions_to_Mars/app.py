from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


# Use flask_pymongo to set up mongo connection locally 
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)


@app.route("/")
def home(): 
    mongo_mars = mongo.db.mars.title
    return render_template("index.html", mongo_mars=mongo_mars)

@app.route("/scrape")
def scrape(): 

    title = mongo.db.title
    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)

