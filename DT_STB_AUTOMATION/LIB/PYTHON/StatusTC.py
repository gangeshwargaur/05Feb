
# StatusTC.py
import json
import requests
def status (execution_id, status):
statusres = ("execution_id" : execution_id, "status": status} Post Result (statusres)
return statusres
def Post Result (dict_data): print ("JS, ", dict_data)
url="http://192.168.1.100:5000/update_build_status?build_details="
data = json.dumps (dict_data) print (type (data), "jsondata") x= requests.post(url + data)
return X