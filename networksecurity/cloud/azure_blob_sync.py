from azure.storage.blob import BlobServiceClient, ContainerClient
import os

class AzureBlobSync:
    def __init__(self, connection_string: str, container_name: str):
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        self.container_client = self.blob_service_client.get_container_client(container_name)

    def upload_folder(self, folder_path: str, blob_path_prefix: str = ""):
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                blob_path = os.path.join(blob_path_prefix, os.path.relpath(full_path, folder_path)).replace("\\", "/")

                with open(full_path, "rb") as data:
                    print(f"Uploading {blob_path}")
                    self.container_client.upload_blob(name=blob_path, data=data, overwrite=True)
