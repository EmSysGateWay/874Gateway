import json
import GateWay485
import post

a = GateWay485.GateWay485(7,11)
url = 'http://115.159.121.185'
deviceId = '869'

while True:
    str = a.readline()
    if len(str) > 0 :
        print 'request post to Server:',str
        obj = json.loads(str)
        ret = post.poll(url,obj,'869')
        print 'response from Server:',ret
        a.write(json.dumps(ret))
    