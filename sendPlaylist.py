import requests
import json
import random


def send_request():
    with open('songs.json') as f:
        playlist = json.load(f)
        print(playlist)
        r = requests.post("http://localhost:5000/videos", json=playlist)
        
if __name__ == '__main__':
    send_request()