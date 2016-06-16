import httpclient as nya
import httplib, urllib
import json
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
def report(device_id, data):
	nya_report(device_id, data)
	fat_report(device_id, data)

if __name__=="__main__":  
	#report()
    print 'test fat for 871'
    payload = {
        "pm2.5": 23,
        "HCHO": 25,
        "Temperature": 20,
        "Humidity":71,
        "CO":103,
        "Detect People":123
    }
    fat_871_report_id = 17
    fat_871_device_id = 22
    fat_report(fat_871_report_id, fat_871_device_id, payload)
    print '-------'
    print 'test nya for 871'
    data = {
        "pm2_5": 23,
        "HCHO": 25,
        "Temperature": 20,
        "Humidity":71,
        "CO":103,
        "DetectPeople":123
    }
    nya_871_device_id = 42
    nya_report(nya_871_device_id, data)
