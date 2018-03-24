import uuid
import csv
from azure.storage.blob import BlockBlobService, PublicAccess
import urllib.request
import requests
        
def save_dataset(dataset,id,container_name, account_name, account_key):
    pass

def test_connection(account_name,account_key):
    block_blob_service = BlockBlobService(account_name=account_name,account_key=account_key)
    print(str(block_blob_service))
    print('connected to blob')


def dataset_from_blob(container_name, id, account_name, account_key):
    blob_name = id + '.csv'
    block_blob_service = BlockBlobService(account_name=account_name,account_key=account_key)
    
    snapshotBlob = block_blob_service.snapshot_blob(container_name, blob_name)

    _params = {
        'snapshot': snapshotBlob.snapshot,
        'timeout': 20000,
    }

    s = requests.Session()
    url = 'https://tabarlowtest.blob.core.windows.net/originals/{}'.format(blob_name)


    r = s.get(url, params=_params, stream=True, timeout=20000)

    features = []
    labels = []

    line_index = 0
    for line in r.iter_lines():
        row = line.strip().decode("utf-8").split(',')
        if line_index == 0:
            titles = row
            line_index += 1
        else:
            for i in range(0,len(row)):
                row[i] = float(row[i])
            features.append(row[0:-1])
            labels.append(row[-1])

    return titles,features,labels
    


    
def save_file(file, id, container_name, account_name, account_key):
    block_blob_service = BlockBlobService(account_name=account_name,account_key=account_key)
    block_blob_service.create_container(container_name)
    block_blob_service.set_container_acl(container_name,public_access=PublicAccess.Container)
    block_blob_service.create_blob_from_stream(container_name,id + '.csv',file.stream)


def clean_dataset(self,file):
    pass

def get_dataset(self,file):
    pass
