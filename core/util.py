import requests
import json
from hilda_garde.settings import DB_HOST, DB_KEY


class DBHandler:
    """
    Database operations handler.
    Retrieve, validate and insert data.
    """

    @staticmethod
    def get_data():
        """
        Retrieve stored data on replit database at this service key.
        """
        data = requests.get(f'{DB_HOST}/{DB_KEY}')
        try:
            data = json.loads(data.text)
        except json.decoder.JSONDecodeError:
            data = None

        return data

    @staticmethod
    def insert_data(data):
        """
        Store a serialized list on replit database.
        Returns the http status code of the requested operation.
        """
        payload = DBHandler.validate(data)
        response = requests.post(DB_HOST, data={DB_KEY: payload})

        return response.status_code

    @staticmethod
    def validate(data):
        """
        Stored data is an array that cannot exceeds length 10
        """
        while len(data) > 10:
            # remove oldest insertion (first position)
            data.pop(0)

        return json.dumps(data)
