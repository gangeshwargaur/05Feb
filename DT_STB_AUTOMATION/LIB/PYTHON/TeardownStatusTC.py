

TeardownStatusTC.py
import json
import requests
def Status (execution_id, result, status):
status_res = ("execution_id": execution_id, "result": result) Post Result (status_res)
status tc = ("execution_id": execution_id, "status": status) Post_status (status_tc)
return status_tc, status_res
def Post_status (dict_data): print ("JS, ", dict_data)
url_s= "http://192.168.1.100:5000/update_build_status?build_details=" data_s= json.dumps (dict_data) print (type (data_s), "jsondata") x= requests.post(url_s + data_s)
return X
def Post Result (dict_data): print ("JS, ", dict_data)
url = "http://192.168.1.100:5000/update_build_result?build_details="
data
=
json.dumps (dict_data)
print (type (data), "jsondata")
x = requests.post(url + data)
return X
Status ("1234", "Complete", "PASS")
STB_Functions.robot
*** Keywords ***
TEST SETUP
#Run Keyword
StatusTC. Status $(execution_id}
In Progress
ADB CONNECT $(DEVICE_IP]
CLEAR LOGCAT
TEST TEARDOWN
[Arguments] $(filename}
DUMP LOGCAT
CLICK
HOME
$filename}
#TeardownStatusTC. Status $(execution_id} Pass Completed
TEST FAIL TEARDOWN
[Arguments] $(filename)
DUMP LOGCAT
$(filename)
CLICK HOME