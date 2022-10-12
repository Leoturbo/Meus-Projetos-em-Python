import json

import requests

API_URL = "https://tradestie.com/api/v1/apps/reddit"

class Data:
    def __init__(self, no_of_comments, sentiment, sentiment_score, ticker):
        self.no_of_comments = no_of_comments
        self.sentiment = sentiment
        self.sentiment_score = sentiment_score
        self.ticker = ticker
        
    @classmethod
    def from_json(cls, json_string):
        json_dict = json.dumps(json_string)
        return cls(**json_dict)
    
    def __repr__(self):
        return f'<comments {self.no_of_comments}>'

json_string = requests.get(API_URL).json()

data = Data.from_json(json_string)
print(data[0])