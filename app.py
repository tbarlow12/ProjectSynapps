#!flask/bin/python
from flask import Flask, request, redirect, url_for
from tools import eval, featurizer as fr, storage as st
import uuid
import pdb

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')


@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/models', methods=['GET','POST'])
def choose_models():
    result = 'Got to choose models'
    if request.form.get('skl-linear-regression') is not None:
        result += '<br>skl-linear'
    if request.form.get('skl-logistic regression') is not None:
        result += '<br>skl-logistic'
    return result


@app.route('/new', methods=['GET', 'POST']) #allow both GET and POST requests
def new():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        account_key = request.form.get('account_name')
        account_name = request.form.get('account_key')



        if account_name is None or account_name.strip() == '' or account_key is None or account_key.strip() == '':
            account_name = app.config['ACCOUNT_NAME']
            account_key = app.config['ACCOUNT_KEY']

        clean = True if request.form.get('clean') == 'yes' else False
        
        dataset_file = request.files.get('dataset')

        if dataset_file is None:
            return 'Please provide a dataset'
        
        id = str(uuid.uuid4())
        #TODO Save dataset in blob storage
        st.save_file(dataset_file,id,'originals',account_name,account_key)

        titles, features, labels = fr.get_dataset(dataset_file)

        return fr.get_summary(titles,features,labels)

    return '''
            <table>
              <form method=post enctype=multipart/form-data>
                  <tr>
                    <td>Model Name: </td>
                    <td><input type="text" name="name"></td>
                  </tr>
                  <tr>
                    <td>Email: </td>
                    <td><input type="text" name="name"></td>
                  </tr>
                  <tr>
                    <td>Dataset: </td>
                    <td><input type="file" name="dataset"></td>
                  </tr>
                  <tr>
                    <td>To Be Cleaned: </td>
                    <td><input type="radio" name="clean" value="no" checked> No <input type="radio" name="clean" value="yes"> Yes</td>
                  </tr>
                    <td>Azure Storage Account (optional): </td>
                  <tr>
                    <td>Account Name: </td>
                    <td><input type="text" name="account_name"></td> 
                  </tr>
                  <tr>
                    <td>Account Key: </td>
                    <td><input type="text" name="account_key"></td>
                  </tr>
                  <tr>
                    <td><input type="submit" value="Submit"></td>
                  </tr>
              </form>
            </table>'''

@app.route('/predict/<id>',methods=['GET','POST'])
def predict(id):
    #load model
    #get features from current example
    
    #make prediction
    
    #return prediction
    return ''



if __name__ == '__main__':
    app.run(debug=True)