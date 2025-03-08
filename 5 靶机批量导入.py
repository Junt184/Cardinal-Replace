# coding=utf-8
import copy
import json
lis = [{ "ChallengeID": 1, "TeamID": 1, "IP": "192.168.2.113", "Port": "2200,8000,33060", "SSHPort": "2200", "SSHUser": "root", "SSHPassword": "aB4dEFQGh22Jk4lM", "Description": "ssh,web,mysql" },]
for i in range(2,13): # 2,8 是需要导入7个靶机的场景,
    a = copy.copy(lis[0])
    # a['ChallengeID'] = i
    a['TeamID'] = i
    a['SSHPort'] = str(int(a['SSHPort'] ) + i -1)
    s = a['Port']
    s = list(map(int,s.split(',')))
    s[0] += i-1
    s[1] += i-1
    s[2] += i-1
    a['Port'] = str(s).strip('[').strip(']')
    lis.append(a)
print(json.dumps(lis))
