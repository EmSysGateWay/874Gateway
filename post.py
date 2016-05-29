import requests
import json
import time

url = 'http://localhost'
#url = 'http://112.124.2.37'
data = {"auth_id": "id","auth_key": "key","device_id": "id"}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
report = requests.post(url+'/api/report', data=json.dumps(data), headers=headers)
print report.status_code

count = 1
s = data['auth_id'] 
while count <= 10:
    data['auth_id'] += str(count)
    poll = requests.post(url+'/api/poll', data=json.dumps(data), headers=headers)
    response = json.loads(poll.text)
    
    print 'new messages'
    for x in response:
    	print 'message:%s target:%s' %(x['message'],x['target'])
    time.sleep(1)
    count += 1    