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
    
    path = request.form["link"]
    
    path = [path]
    print(path)
    
    res, flair = process(list(path))
    
    print("[INFO] Result: \n", res[path[0]])
    return(render_template("result.html", prediction = res[path[0]], actual = flair))
    

@app.route('/automated_testing', methods = ["POST"])
def predict_file():
    
    for i in request.files:
        file = request.files[i]
        
        urls = file.read()
        urls = urls.decode("utf-8").split("\n")
        print(urls)
        urls = [i.replace("\r", "") for i in urls]
        print("length: ", len(urls))
        
        res = process(urls)
        
        print(res)
                
        
    
    return(jsonify(res))
        

app.run(threaded = True)
