#!flask/bin/python
from flask import Flask, request, redirect, url_for
from tools import eval, featurizer as fr, storage as st
import uuid
import pdb

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')

st.test_connection(app.config['ACCOUNT_NAME'],app.config['ACCOUNT_KEY'])

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/train',methods=['POST'])
def train():
    cleaned = True
    content = request.get_json()
    pdb.set_trace()
    account_name = app.config['ACCOUNT_NAME']
    account_key = app.config['ACCOUNT_KEY']

    id = str(uuid.uuid4())
    if request.method == 'POST' and len(request.files) > 0:
        file = request.files['file']
        cleaned = True
        original_file_container = 'original_files_clean' if cleaned else 'original_files_unclean'
        st.save_file(file, id, original_file_container, account_name,account_key)



@app.route('/predict/<id>',methods=['GET','POST'])
def predict(id):
    #load model
    #get features from current example
    
    #make prediction
    
    #return prediction
    return ''



if __name__ == '__main__':
    app.run(debug=True)