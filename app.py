#!flask/bin/python
from flask import Flask, request, redirect, url_for
from tools import eval, featurizer as fr, storage as st
import uuid
import pdb

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')

account_name = app.config['ACCOUNT_NAME']
account_key = app.config['ACCOUNT_KEY']


@app.route('/')
def index():
    return '<a href="/new">Create a new model</a>'

@app.route('/choosemodels/<id>', methods=['GET','POST'])
def choose_models(id):
    result = 'Got to choose models'

    titles, features, labels = st.dataset_from_blob('originals',id,account_name,account_key)


    if request.form.get('skl-linear-regression') is not None:
        result += '<br>skl-linear'
    if request.form.get('skl-logistic regression') is not None:
        result += '<br>skl-logistic'
    return result

distinct_limit = 10

def get_distinct_count(items):
    result = set()
    for item in items:
        result.add(item)
        if len(result) > distinct_limit:
            return '{}+'.format(distinct_limit)
    return '{}'.format(len(result))

def get_summary(titles,features,labels,id):
    title_row = '<td></td>'
    for title in titles:
        title_row += '<h2><td>{}</td></h2>'.format(title)
    summary = '<tr>{}</tr>'.format(title_row)

    distinct_row = '<td>Distinct Values</td>'
    for i in range(0,len(features[0])):
        distinct_count = get_distinct_count([row[i] for row in features])
        distinct_row += '<td>{}</td>'.format(distinct_count)

    label_distinct_count = get_distinct_count(labels)
    distinct_row += '<td>{}</td>'.format(label_distinct_count)

    summary += '<tr>{}</tr>'.format(distinct_row)

    


@app.route('/new', methods=['GET', 'POST']) #allow both GET and POST requests
def new():
    if request.method == 'POST':  #this block is only entered when the form is submitted

        dataset_file = request.files.get('dataset')
        if dataset_file is None:
            return 'Please provide a dataset'
        
        id = str(uuid.uuid4())
        st.save_file(dataset_file, id, 'originals', account_name, account_key)

        titles, features, labels = st.dataset_from_blob('originals',id,account_name,account_key)


        pdb.set_trace()
        result = ''

        if request.form.get('skl-lin-reg') is not None:
            result += '<br>skl-linear'
        if request.form.get('skl-log-reg') is not None:
            result += '<br>skl-logistic'
        return result

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
                        <td><input type="checkbox" name="skl-lin-reg" value="yes"> SKLearn Linear Regression</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox" name="skl-log-reg" value="yes"> SKLearn Logistic Regression</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox" name="skl-svm" value="yes"> SKLearn SVM</td>
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