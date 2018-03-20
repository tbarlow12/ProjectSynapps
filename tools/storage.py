import uuid

class Storage(object):

    

    def __init__(self,config):
        self.account_name = config['ACCOUNT_NAME']
        self.account_key = config['ACCOUNT_KEY']

def add_new_dataset(request, cleaned, config):
    id = str(uuid.uuid4())
    if request.method == 'POST' and len(request.files) > 0:
        file = request.files['file']
        container_name = 'clean_datasets' if cleaned else 'unclean_datasets'
        save_file(file,id,container_name)
        
        
def save_file(file, id, container_name, config):

    