import httpclient as nya
import httplib, urllib
import json
import GateWay485

#nya
nya_auth_id = 15
nya_auth_key = "d7fe7b0a3c1dbde58e251d3aafc4954f"
nya_client = nya.HTTPClient(nya_auth_id, nya_auth_key, "nya.fatmou.se")
#fat
fat_auth_id = 6
fat_auth_key = '4788cab347ad9b13baa24edee1554ed3'
fat_client = httplib.HTTPConnection("fat.fatmou.se", 80, timeout=30)

def nya_report(device_id, data):
	ret = nya_client.report(device_id, data)
	print ret

def fat_report(report_id, device_id, data):
    # temp = []
    # for key, value in data.iteritems():
    #     temp.append('"%s":"%s"'%(key, str(value)))
    # payload_str = reduce(lambda x,y:x+','+y, temp)
    # payload_str = '{'+payload_str+'}'

    report_data = {
        'auth_id': fat_auth_id,
        'auth_key': fat_auth_key,
        'device_id': device_id,
        'report_id': report_id,
        'payload': json.dumps(data)
    }

    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    params = urllib.urlencode(report_data)
    fat_client.request("POST", "/api/report", params, headers)

    response = fat_client.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders()

#report_id for fat
def report(data):
	nya_report(45, data)
	fat_report(25, 12, data)

if __name__=="__main__":
	a = GateWay485(7,11)
	while True:
		str = a.readline()
		if len(str) > 0:
			print 'Receive from 869 module :',str
			obj = json.loads(str)
			report(obj)
	# data = {"Date":"2016-xx-xx xx:xx:xx","User":"xxxxxxxxxx","Identity":"Success"}
	# # nya_report(45,data)
	# report_id = 25
	# device_id = 12
	# fat_report(report_id, device_id, data)
