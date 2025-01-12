import os
import json
import sys
from dotenv import load_dotenv
load_dotenv()

import certifi

mdbrl = os.getenv("MONGO_DB_URL")
print(mdbrl)

ca = certifi.where()

import numpy as np
import pandas as pd
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_convert(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    def insert_data_to_db(self, records, db, collection):
        try:
            self.db = db
            self.records = records
            self.collection = collection
            self.mongo_client = pymongo.MongoClient(mdbrl, tlsCAFile=ca)
            self.db = self.mongo_client[self.db]
            self.collection = self.db[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__=='__main__':
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="SamarthGarg"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convert(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_to_db(records,DATABASE,Collection)
    print(no_of_records)