import httplib, urllib, json
auth_id = 6
auth_key = '4788cab347ad9b13baa24edee1554ed3'

device_id_871 = 22
report_id_871 = 17

def fat_report(report_id, device_id, payload):
    temp = []
    for key, value in payload.iteritems():
        temp.append('"%s":"%s"'%(key, str(value)))
    payload_str = reduce(lambda x,y:x+','+y, temp)
    payload_str = '{'+payload_str+'}'

    report_data = {
        'auth_id': auth_id,
        'auth_key': auth_key,
        'device_id': device_id,
        'report_id': report_id,
        'payload': payload_str
    }

    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    httpClient = httplib.HTTPConnection("fat.fatmou.se", 80, timeout=30)

    params = urllib.urlencode(report_data)
    httpClient.request("POST", "/api/report", params, headers)

    response = httpClient.getresponse()
    print '--------'
    print response.status
    print response.reason
    print response.read()
    print response.getheaders()

if __name__=="__main__":    
    payload = {
        "pm2.5": 23,
        "HCHO": 25,
        "Temperature": 20,
        "Humidity":71,
        "CO":103,
        "Detect People":2
    }

    fat_report(report_id_871, device_id_871, payload)