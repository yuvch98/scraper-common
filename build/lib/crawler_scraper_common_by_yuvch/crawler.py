from abc import ABC
import json
from pymongo.mongo_client import MongoClient
import os
import datetime


class Crawler(ABC):
    def __init__(self, url):
        self.data = {}
        self.url = url
        self.uri = os.getenv("MONGO_URI")
        self.db_name = 'jobs'
        self.collection_name = None
        self.client = None
        self.collection = None

    def export_json(self) -> str:
        json_data = json.dumps(self.data, indent=4, ensure_ascii=False)
        return json_data

    def import_json(self) -> None:
        try:
            json_data = json.load(open(f"output_files/{type(self).__name__}.json", "r", encoding='utf-8'))
            for item in json_data:
                print(json_data[item])
        except FileNotFoundError:
            print("No such json file found in system")

    def _connect_to_mongo(self):
        """Establish and cache the MongoDB connection."""
        if not self.client:
            self.client = MongoClient(self.uri)
            self.collection = self.client[self.db_name][self.collection_name]  # Use a fixed collection name

    def move_to_mongo(self):
        """Insert new job data into MongoDB."""
        self._connect_to_mongo()
        for item in self.data:
            if self.collection.find_one({'url': item}):
                continue
            doc = {
                'url': item,
                'job_title': self.data[item]['title'],
                'location': self.data[item]['location'],
                'responsibilities': self.data[item]['Responsibilities'],
                'requirements': self.data[item]['Requirements'],
                'active': True,
                'date': datetime.datetime.now().strftime("%D")
            }
            self.collection.insert_one(doc)

    def update_mongo(self):
        """Update job data in MongoDB to mark inactive jobs."""
        self._connect_to_mongo()
        keys = self.data.keys()
        for doc in self.collection.find():
            if doc['url'] not in keys:
                self.collection.find_one_and_update({'url': doc['url']},
                                                    {'$set': {"active": False}})
