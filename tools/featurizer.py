import csv
import pdb


def get_dataset(dataset_file):
    pdb.set_trace()
    lines = dataset_file.readlines()
    features = []
    labels = []
    pdb.set_trace()
    titles = lines[0].strip().decode("utf-8").split(',')
    for line in lines[1:]:
        row = line.strip().decode("utf-8").split(',')
        for i in range(0,len(row)):
            row[i] = float(row[i])
        features.append(row[0:-1])
        labels.append(row[-1])
    return titles,features, labels 




    