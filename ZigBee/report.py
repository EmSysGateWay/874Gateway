import json
import binaryClient
import httpreport

def nya_report(device_id, data, HttpOrBinary=True):
	if HttpOrBinary:
		httpreport.nya_report(device_id, data)
	else:
		binaryClient.nya_report(device_id, data)

def fat_report(report_id, device_id, data, HttpOrBinary=True):
	if HttpOrBinary:
		httpreport.fat_report(report_id, device_id, data)
	else:
		binaryClient.fat_report(report_id, device_id, data)

if __name__=="__main__":  
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
    fat_report(fat_871_report_id, fat_871_device_id, payload, True)
    print '----------------'
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
    nya_report(nya_871_device_id, data, True)
    print '----------------'





		



