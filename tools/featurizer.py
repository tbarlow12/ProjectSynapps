import csv
import pdb

distinct_limit = 10

def get_dataset(dataset_file):
    lines = dataset_file.readlines()
    features = []
    labels = []
    titles = lines[0].strip().decode("utf-8").split(',')
    for line in lines[1:]:
        row = line.strip().decode("utf-8").split(',')
        for i in range(0,len(row)):
            row[i] = float(row[i])
        features.append(row[0:-1])
        labels.append(row[-1])
    return titles,features, labels 

def get_distinct_count(items):
    result = set()
    for item in items:
        result.add(item)
        if len(result) > distinct_limit:
            return '{}+'.format(distinct_limit)
    return '{}'.format(len(result))

def get_summary(titles,features,labels):
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

    return '''<table>{}</table>
              <table>
                <form method=post enctype=multipart/form-data action="/models">
                    <tr></tr>
                    <tr>
                        <td><input type="checkbox" name="skl-linear-regression" value="yes"> SKLearn Linear Regression</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox" name="skl-logistic-regression" value="yes"> SKLearn Logistic Regression</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox" name="skl-svm" value="yes"> SKLearn SVM</td>
                    </tr>
                    <tr>
                        <td><input type="submit" value="Submit"></td>
                    </tr>
                </form>
              </table>'''.format(summary)

    