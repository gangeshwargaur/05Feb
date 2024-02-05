

File:
#Purpose:
selection as Text
#copyrights
#Owner:
#Notes:
getMethod.py
or Image, this module is imported in stb.py
Python script to get the comparison method from user
(c) LTTS
Cogmation Team
First Created on 01-Feb-2019 By Cogmation
#Developer Note: All the commented lines are used for code debugging.
# Import Section
from tkinter import⚫
class ActivationFrame (Frame) :
def __init__(self, master):
Frame._init__(self, master)
for method in ["Text", "Image"]:
button Button (self, text-method, command-lambda m-method:
self.key_clicked (m, master))
button.grid (columnspan=2)
self.grid()
def key clicked (self, method, master):
if method == "Text": self.method="Text"
elif method = "Image":
self.method = "Image"
button Button (self, text="Quit", command-master.destroy).grid() return (self.method)
def getFrame():
root Tk ()
return root
StatusTC.py
import json
import requests
def status (execution_id, status):
statusres = ("execution_id" : execution_id, "status": status} Post Result (statusres)
return statusres
def Post Result (dict_data): print ("JS, ", dict_data)
url="http://192.168.1.100:5000/update_build_status?build_details="
data = json.dumps (dict_data) print (type (data), "jsondata") x= requests.post(url + data)
return X