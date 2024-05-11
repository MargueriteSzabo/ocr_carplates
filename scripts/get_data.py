from google.cloud import storage
import os
from pathlib import Path

path_to_file = os.environ.get("LOCAL_DATA_PATH")
bucket_name = os.environ.get("BUCKET_NAME")
json_key = os.environ.get("JSON_KEY")


def upload_bucket(blob_name, path_to_file, bucket_name):
    """ Upload data to a bucket"""

    # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json(
        json_key)

    #print(buckets = list(storage_client.list_buckets())

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)

    #returns a public url
    return f'{blob_name} done ✅'


def upload_data():
    path = Path(os.getcwd())
    mypath = str(path.parent.absolute())+'/data/train'
    onlyfiles = [f for f in os.listdir(mypath)]
    for file in onlyfiles:
        path_to_file = mypath + '/' + file
        upload_bucket(file, path_to_file, bucket_name)
    return f'Data uploaded in {bucket_name}✅'



def download_data():
    # Initialise a client
    storage_client = storage.Client.from_service_account_json(
        json_key)
    # Create a bucket object for our bucket
    bucket = storage_client.get_bucket(bucket_name)
    # Create a blob object from the filepath
    for bloby in storage_client.list_blobs(bucket_name):
        blob = bucket.blob(bloby)
        # Download the file to a destination
        path = Path(os.getcwd())
        destination_file_name = str(path.parent.absolute())+'/data/train/'
        blob.download_to_filename(destination_file_name)


if __name__ == '__main__':
    upload_data()
