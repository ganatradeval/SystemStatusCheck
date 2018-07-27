from platform import system as system_name
from subprocess import getstatusoutput
import json,urllib3

host = ['192.168.0.1','192.168.0.2'] #Change ip/hostname of your server/application

SLACK_CHANNEL="#<Slack Channel Name>"
HOOK_URL="<URL of Channel>"

#To limit ping request
param = '-n' if system_name().lower()=='windows' else '-c'

command = [ ['ping', param, '1', i]	for i in host]


message=''
for i in command:
	status,out = getstatusoutput(i)
	if status == 1 :
		print (i[3], "is NOT working")
		message += i[3] + "is NOT working\n"
	else:
		if out.find('time=') == -1:
			print (i[3], "is NOT working\n")
			message += i[3] + "is NOT working"
		else:
			print (i[3], "is working fine")
			
#Create format of slack message request
slack_message = {
       'channel': SLACK_CHANNEL,
       'text': message,
       'username': 'System Check',      #you cam modify this settings
       'icon_emoji': ":ghost:"          #also this can be modified
   }

#Send the POST request using urllib
http=urllib3.PoolManager()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)     #optional but use if Shows warning of Certificate 
response = http.request('POST', HOOK_URL, headers={'Content-Type':'application/json'}, body=json.dumps(slack_message) )
