#!flask/bin/python
from flask import Flask, request, redirect, url_for
from tools import eval, featurizer, storage, loader
import pdb
import uuid
import json

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/predict/<id>',methods=['GET','POST'])
def predict(id):
    #load model
    model = storage.load_model(id)

    
    #get features from current example
    
    #make prediction
    
    #return prediction
    return ''



if __name__ == '__main__':
    app.run(debug=True)