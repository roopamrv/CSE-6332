import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def upload_blob(local_file_name):
    connect_str = 'DefaultEndpointsProtocol=https;AccountName=cse6332store;AccountKey=q7DeZ0YB2fSxl2j4iHQnuypzUcRzZ8W28EtSN7c1xmv7ggC4aozvWW1UQuZVAto4CTEg0xaZ+zEt+ASt0Mx9Hg==;EndpointSuffix=core.windows.net'
    container_name = 'mycontainer'
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        local_path = "./uploads"
        upload_file_path = os.path.join(local_path, local_file_name)
        print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)
        local_file_name = str(uuid.uuid4()) + ".jpg"

        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
        # Upload the created file
        with open(file=upload_file_path, mode="rb") as data:
            blob_client.upload_blob(data)
        return 'Success', local_file_name
    except Exception as ex:
        return 'Exception:', ex