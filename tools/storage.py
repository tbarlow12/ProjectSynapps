import uuid
import csv
from azure.storage.blob import BlockBlobService, PublicAccess
        
def save_dataset(dataset,id,container_name, account_name, account_key):
    pass

def test_connection(account_name,account_key):
    block_blob_service = BlockBlobService(account_name=account_name,account_key=account_key)
    print(str(block_blob_service))
    print('connected to blob')

    
def save_file(file, id, container_name, account_name, account_key):
    block_blob_service = BlockBlobService(account_name=account_name,account_key=account_key)
    block_blob_service.set_container_acl(container_name,public_access=PublicAccess.Container)


def clean_dataset(self,file):
    pass

def get_dataset(self,file):
    pass
