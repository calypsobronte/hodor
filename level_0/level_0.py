#!/usr/bin/python3
""" Write a script or a program that votes 1024 times for your id here: http://158.69.76.135/level0.php. """
import requests

url = "http://158.69.76.135/level0.php"

with requests.session() as client:
	data = {"id": 1992, "holdthedoor": "submit"}
	for cont in range(1024):
		client.post(url, data)
