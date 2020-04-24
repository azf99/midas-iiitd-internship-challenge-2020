from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from utils import *


app = Flask(__name__)

CORS(app)

@app.route('/')
@app.route('/index')
def index():
    return(render_template("index.html"))



@app.route('/predict', methods = ["POST"])
def predict():
    '''
    Takes the post URL from thee HTML form, at the homepage
    and sends it for scraping and prediction
    '''
    
    path = request.form["link"]
    
    path = [path]
    print(path)
    
    res, flair = process(list(path))
    
    print("[INFO] Result: \n", res[path[0]])
    return(render_template("result.html", prediction = res[path[0]], actual = flair))
    

@app.route('/automated_testing', methods = ["POST"])
def predict_file():
    '''
    Takes the text file from the POST request, processes it and
    sends all the post URLs for sraping and prediction
    '''
    
    
    file = request.files["upload_file"]
    
    urls = file.read()
    urls = urls.decode("utf-8").split("\n")
    #print(urls)
    urls = [i.replace("\r", "") for i in urls]
    #print("length: ", len(urls))
    
    res, f =  process(urls)
    
    #print(res)
    
    return(jsonify(res))
        

app.run(threaded = True)
