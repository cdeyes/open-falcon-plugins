#!/usr/bin/python
import time
import socket
import json
rl=[]
st=int(time.time())
va=st+100
hn=socket.gethostname()
result={ 'endpoint' : hn,
         'tags' : '',
         'timestamp' : st,
         'metric' : 'sys.ops.test',
         'value' : va,
         'counterType' : 'GAUGE',
         'step' : 30
       }
#one two three four
rl.append(result)
print json.dumps(rl)
