import requests
import json
import time

auth_id = '874'
auth_key = '874'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def report(url, payload, device_id):
	data = {"auth_id": auth_id,"auth_key": auth_key,"device_id": device_id, "payload":payload}
	response = requests.post(url+'/api/report', data=json.dumps(data), headers=headers)
	print 'report status: ', response.status_code

def poll(url, payload, device_id):
	data = {"auth_id": auth_id,"auth_key": auth_key,"device_id": device_id, "payload":payload}
	response = requests.post(url+'/api/poll', data=json.dumps(data), headers=headers)
	return response.json()

### Example ###

# # report
# # for zigbee
# url = 'http://localhost'
# payload = {}
# payload['testfield'] = 'testdata'

# report(url, payload, 'FromZigBee')


# # poll
# # for 485
# # get user privilege
# payload = {
# 	'RequestType':'auth',  
#     'DeviceId':'869'
# }
# response = poll(url, payload, '869')
# print response.json()

# # upload log
# payload = {
# 	'RequestType':'upload',  
#     'DeviceId':'869',
#     'Data':{  
#         'time':'2016-05-29-14-40-23',  
#         'id':'xx',  
#         'legal':'y',  
#         'logInOrOut':'in'  
#     }  
# }
# response = poll(url, payload, '869')
# print response.json()




# data = {"auth_id": "id","auth_key": "key","device_id": "id", "payload":payload}
# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# report = requests.post(url+'/api/report', data=json.dumps(data), headers=headers)
# print report.status_code


# #poll
# count = 1
# s = data['auth_id'] 
# while count <= 10:
#     data['auth_id'] += str(count)
#     poll = requests.post(url+'/api/poll', data=json.dumps(data), headers=headers)
#     response = json.loads(poll.text)
    
#     print 'new messages'
#     for x in response:
#     	print 'message:%s target:%s' %(x['message'],x['target'])
#     time.sleep(1)
#     count += 1    