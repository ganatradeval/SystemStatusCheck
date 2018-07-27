# Health Check by Ping 

This simple script will ping you given hosts and returns message onto slack if server is down(Ping is not working).



## Prerequisits
* Tested on Windows/Linux
* It is designed on python 3.6 but it will work on python 3. (For python2 it requires few syntaxchanges)
* urllib3 for POST to slack
* IP/Hostname 

## Input Variables 
* host = [<IP_Address here>] string Seperated by comma
```
["192.168.0.1","192.168.0.2"]
```
* SLACK_CHANNEL="<Channel Name>"
* HOOK_URL= "<URL of channel>"
## Use
Put this as a cron job or schedule in windows or cron in linux. 

Suggest me if you require this to send logs on CloudWatch using custom matrix. They already have matrix for this so it would be good for personal use.
