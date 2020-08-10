#coding=utf8
import sys
import json

reqDict = {}

file = sys.argv[1]
with open(file) as f:
  for line in f.readlines():
     obj = json.loads(line)
     msgObj = json.loads(obj['content'])

     const requestId = msgObj['requestId']
     print requestId

     msgSet.add(msgObj['msg'])
     splits = msgObj['msg'].split(' ')
     fromUsers.add(splits[3])
     toUsers.add(splits[4])

print '发消息人数: ' + str(len(fromUsers)) + '收消息人数: ' + str(len(toUsers))
print len(msgSet)
