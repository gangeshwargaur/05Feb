# Import Section

import os
import subprocess
import cv
import numpy as np
import getMethod
import pytesseract
# from cmdSendDevice import *
from importlib.machinery import SourceFileLoader
from tkinter import *
import sqlite3
import pandas as pd
from datetime import datetime
import time
import imagehash
from PIL import Image

class STB(object):

    compImagePath = ""
    refImagePath = ""
    referenceImage = ""
    capturedImage = ""
    threshold = 0
    cropping = False
    image = None
    clone = None
    autocal = None
    image2save = ""
    imageName = ""
    xyCod = ""
    coordinates = []
    #cmdSendDev = None
    directory = ""
    only_alpha = ""
    port0 = list()
    port1 = list()
    port2 = list()
    port3 = list()
    overall_port_0 =list()
    overall_port_1 = list()
    overall_port_2 = list()
    overall_port_3 = list()
    var = ""
    def __init__(self, directory):
        """
        Contains reference image path, compare image path
        """
        print("path: ",directory)
        self.directory = directory
        config_folder = r'TestScripts/VARIABLES/Config.py'
        config1 = os.path.join(directory,config_folder)
        print(config1)
        cfg=SourceFileLoader("Config",config1).load_module()
        self.name = "STB"
        # self.stbData = cfg.legacy

        self.autocal = cfg.autocal

        print(self.autocal}

        # self. socket = cfg. legacy! "socket"}

        # self.genericbata = cfg.generic

        self.threshold = float(cfg.threshold)

        print(self.threshold)

        self.hdmiPorts = cfg.hdmiports

        print(self.hdmiPorts)

        self.deviceip = cfg.DEVICE_IP

        print(self.deviceip)

        # path for reference image

        self.refImagePath =

        os.getcwd() + "/" + "TestScripts" + "/" + "IMAGES" + "/" + "STB" + "/" + "Reference_Images”+"/"

        self.compImagePath =

        os.getcwd() + "/" + "TestScripts" + "/" + "IMAGES" + "/" + "STB" + "/"  # path for

        capturedimage
        s
        self.timestamp = time.strftime("%Y%m%d %H%M%S", time.gmtime())

        # self.cmdSendDev = getCmdSendDev(self.stbData, self.genericData)

        self.cwd = os.getcwd()

        self.table
        name = ‘STB’


        self.deviceName = "STB"

        self.create_table()

        def create_table(self):

         """

        Creating Table to store the cropped image coordinates, image

         comparison method and image name

        table gets created inside current working directory inside LIB\DB\
    ﻿path
"""
curr_dir os.getcwd ()
print (curr_dir)
db_path= os.path.join(curr_dir, 'TestScripts/LIB/DB/refImage.db')
conn = sqlite3.connect (db_path)
print("opened database")
curs =  conn.cursor()
print ("table_name = STB")
query0 = CREATE TABLE IF NOT EXISTS + self.table_name + (imgName TEXT, xyCoordinates TEXT, method TEXT); &#039;
curs.execute(query))
print (query))
#def press (self, cmd):
www
This Keyword will send remote signals to setup box devices
print (&quot;command: &quot;, cmd, type (cmd)) self.cmdSendDev.sendCommand (cmd)
#def list_datasets (self):
#
data file.
This Keyword will list the available datasets of the remote signal
www
#self.cmdSendDev. listdatasets ()
#def start signals (self):
#
This Keyword will open socket connection to send remote signals from irNet Box.
#
self.cmdSendDev. OpenSocket (self.socket, 40000)
#def end_signals (self):
#
This Keyword will close socket connection after remote signals
sent from irNetBox.
www
# self.cmdSendDev. CloseSocket ()
def compareText (self, imgcrop):
screen.
www
This Keyword will compare the text that is extracted from the
print(&quot;In compareText&quot;)
image = cv2.imread (imgcrop)
if image is not None:
gray = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY) name = &quot;temp_&quot;+self.hdmi Ports # client machine filename = &quot;).jpg&quot;.format (name) # client machine
# filename - &quot;().jpg&quot;.format(&quot;temp&quot;) # bangalore machine cv2.imwrite (filename, gray)
#print (&quot;imgcrop&quot;, filename) img1= cv2.imread(filename)
﻿img1- cv2.resize(img1, None, fx-2, fy-2,
interpolation-cv2.INTER CUBIC)
thresh = cv2.threshold (img1, 83, 255, cv2.THRESH_BINARY_INV) [1] text pytesseract.image_to_string (thresh, lang=eng&#039;) print(&quot;text&quot;, text)
imagel cv2.imread(self.referenceImage)
gray!= cv2.cvtColor(imagel, cv2.COLOR_BGR2GRAY) namel &quot;templ &quot;+self.hdmi Ports #client machine filenamel &quot;1.jpg&quot;.format (namel) #client machine filenamel - &quot;().jpg&quot;.format(&quot;templ&quot;) cv2.imwrite (filenamel, grayl)
#print (&quot;referenceimage&quot;, filenamel)
img2
img2
cv2.imread(filenamel)
cv2.resize (img2, None, fx-2, fy-2,
interpolation-cv2.INTER_CUBIC)
threshi cv2.threshold (img2, 83, 255,
cv2.THRESH BINARY INV) [1]
#banaglore machine
textl pytesseract.image_to_string (threshi, lang=&#039;eng&#039;) print (&quot;Reference text1&quot;, text1)
if text.lower()
else:
return &quot;Pass&quot;
return &quot;Fail&quot;
if image is None:
text1.lower():
raise ValueError(&quot;The given image or path is not found, Check
the given image is available in the path&quot;)
def refImgCrop (self):
www
This function is used to return the coordinates of reference Image which is capture during the True condition
database - os.getcwd ()+&#039;/TestScripts/LIB/DB/refImage.db&#039; print (database)
conn = sqlite3.connect (database)
curs= conn.cursor()
print(&quot;inside ref&quot;)
query= select xyCoordinates from self.table_name +
imgName = &quot; + self.imageName+&quot;&quot;; &quot;
print (query)
curs.execute(query)
self.xyCod curs.fetchone ()
print (self.xyCod)
self.coordinates = []
self.coordinates = list (map (str, self.xyCod[0].split(&#039;,&#039;)))
print (self, coordinates)
return self.coordinates
def select_method (self):
www
where
This function is used to choose Image comparison method or text comparison method
www
﻿root_activation frame =
getMethod.getFrame()
1f getMethod. ActivationFrame (root_activation frame) root_activation frame.mainloop()
print((&quot;1f method&quot;, 1f.method)) return 1f.method
def click_and_crop (self, event, x, y, flags, param):
www
Performs Click and Crop and stores the cropped coordinates in database along with the image name and comparison
method.
if the left mouse button was clicked, record the starting (x, y) coordinates and indicate
#that cropping is being performed
if event
cv2.EVENT_LBUTTONDOWN:
self.refpt = {(x, y)]
self.cropping =True
# check to see if the left mouse button was released elif event = cv2.EVENT_LBUTTONUP:
# record the ending (x, y) coordinates and indicate that the
cropping operation is finished
255, 0), 2)
self.refPt.append((x, y))
self.cropping = False
# draw a rectangle around the region of interest
cv2.rectangle(self.image, self.refPt [0], self.refPt(1), (0,
cv2.imshow(&quot;image&quot;, self.image)
if len(self.refPt) == 2:
roi = self.clone(self.refPt [0][1]: self.refPt [1] [1],
self.refPt[0][0]: self.refPt [1][0]]
imgName =
cv2.imshow(&quot;ROI&quot;, roi)
cv2.imwrite (self.image2save, roi)
print (&quot;inside click and crop&quot;) self.method= self.select_method () print(self.method)
print(&quot;entering db&quot;)
print (os.path.dirname (os.getcwd())) to_dir= os.path.dirname (os.getcwd ()) print (os.getcwd())
curr= os.getcwd ()
database
curr+r/TestScripts/LIB/DB/refImage.db&#039;
# print (&quot;database
&quot; + database)
conn = sqlite3.connect (database)
#print (&quot;opened database&quot;)
curs conn.cursor()
queryl
&#039;select count(*) from + self.table_name + where
+ self.imageName+&#039;&quot;;&#039;
#print (queryl)
curs.execute (query1)
val curs.fetchone ()
#print (val [0])
if val[0] = 0:
query2 insert into + self.table_name + values
(&quot;&#039;+self.imageName+&#039;&quot;,&quot;&#039; + \
&quot;&#039;+str(self.refPt)+&#039;&quot;,+!&quot;
# print (query2)
+self.method+&#039;&quot;);&quot;
﻿else:
curs.execute(query2)
str(self.refPt) +
query? &#039;update+self.table_name + set xyCoordinates &quot;, method=&quot;self.method&quot; where imgName-
&quot;self.imageName+&quot;&quot;;&quot;
#print (query2)
curs.execute (query2)
conn.commit()
def auto_calibration (self, captured_image):
This function is called from compare_image keyword in True
condition.
print(&quot;inside auto_calibration&quot;)
self.imageName captured_image
print (self.imageName)
self.image2save self.refimagePath+ captured_image
print(&quot;The selected ROI is saved in this path: &quot;, self.image2save) captured_image- self.compImagePath
print (captured_image)
captured_image
load the image, clone it, and setup the mouse callback function self.image cv2.imread(captured_image)
if self.image is not None:
print (&quot;reading image&quot;) self.cloneself.image.copy() print (&quot;cloning image&quot;)
cv2.namedWindow(&quot;image&quot;)
self.clone - cv2.resize(self.clone, (960, 540)) self.image cv2.resize(self.image, (960, 540)) print(&quot;resizing image&quot;)
try:
cv2.setMouseCallback(&quot;image&quot;, self.click_and_crop)
cv2.imshow(&quot;image&quot;, self.image)
key cv2.waitKey(0)
cv2.destroyAllWindows()
return &quot;Pass&quot;
except:
return &quot;Fail&quot;
if self.image is None:
raise ValueError(&quot;The given image or path is not found, Check
the given image is available in the path&quot;)
def get_image (self, captured Image):
This function is called from capture_image keyword to get the images from capture card.
www
image_name_list = list()
var false list ()
if self.autocal is True:
self.ImageName = capturedImage + &quot;.jpg&quot; port=&quot;/dev/video&quot;+ str(self.hdmi Ports) print (self.hdmi Ports)
print (port)
test subprocess. Popen ([&quot;gst-launch-1.0&quot;,
&quot;v412sre&quot;,
f&quot;device (port)&quot;, &quot;num-buffers-1&quot;, &quot;1&quot;, &quot;jpegenc&quot;, &quot;!&quot;, &quot;filesink&quot;, &quot;location=&quot;+self.compImagePath+self.ImageName], stdout=subprocess.PIPE,
stderr=subprocess.PIPE)
﻿

else:
".jpg"
test.communicate()
camera cv2.VideoCapture (port)
ret, frame
if ret:
camera.read()
loc= self.compImagePath+self.ImageName print (loc)
cv2.imwrite (loc, frame)
camera.release()
cv2.destroyAllWindows()
return self. ImageName
#for n in self.hdmi Ports:
self.ImageName- capturedImage ++ str(self.hdmi Ports) +
image_name_list.append(self.ImageName)
port = "/dev/video"+str(self.hdmi Ports) print("capture false", port)
#print (image_name_list, len (image_name_list)) subprocess.Popen (["gst-launch-1.0",
test -
"v412src",
f"device (port)", "num-buffers-1", "1", "jpegenc", "1", "filesink", "location="+self.compImagePath+self.ImageName], stdout=subprocess.PIPE,
stderr-subprocess.PIPE)
camera = cv2.VideoCapture (port)
ret, frame
if ret:
camera.read()
loc= self.compImagePath+self.ImageName print (loc)
cv2.imwrite (loc, frame)
camera.release()
cv2.destroyAllWindows ()
time.sleep(5)
print("after test")
print (self.compImagePath+self. ImageName)
if os.path.getsize (self.compImagePath+self. ImageName) == 0: time.sleep (60)
if os.path.getsize(self.compImagePath+self. ImageName) 0: print("Please check if working stb is connected to
capture card!!!")
else:
var false.append("False")
return var false
#test.communicate()
return image_name_list
else:
#test.communicate()
return image_name_list
#return image_name_list
def Scheduling (self):
This will return the autocal value True or False
"""
print (self.autocal)
return self.autocal
#def hdmi_port (self, hdmiports):
﻿

be used.
#
#
#
#
This will return the port number of the capture card which is to
self.hdmi Ports hdmiports
print ("self.hdmi Ports:", self.hdmi Ports) return self.hdmi Ports
#def irport_range (self, irport_range_port):
#
#
#
#
www
This will return the ir emitters value which is to be used.
print (irport_range_port)
condition.
return send_irange_port (irport_range_port)
def is Image Found (self, referenceImage, captured Image, threshold_value): This function is called from the compare_image keyword during False and the image comparison will happen here if the method chosen is The parameters threshold value can be modified as per the required accuracy level.
"image".
condition
:param reference Image: captured reference image name during True :param capturedImage: captured live image from STB during false :param threshold value: value ranges from 0.1 to 1.0
condition
self.imageName referenceImage
self.referenceImage self.refImagePath+reference Image
print (self.referenceImage)
self.capturedImage = self.compImagePath+capturedImage print (self, capturedImage)
to_dir= os.path.dirname (os.getcwd())
print (to_dir)
print (os.getcwd())
curr= os.getcwd()
database curr+ r'/TestScripts/LIB/DB/refImage.db'
print (database)
conn =
sqlite3.connect (database)
curs conn.cursor ()
query3 -'select method from self.table_name + where imgName
self.imageName + ";"
print (query3)
curs.execute (query3)
self.method = curs.fetchone ()
self.method=self.method [0]
print (self.method)
self.coordinates = self.refImgCrop()
x1 = int(self.coordinates[0].strip("[(")) yl
int(self.coordinates [1].strip(")"))
x2= int(self.coordinates [2].strip(" (")) y2= int(self.coordinates [3].strip(")]"))
print ("In ismagefound")
print (x1)
print (y1)
﻿

print (x2) print (y2)
ret val False
imgcrop
self.compImagePath+r'cropimg_+str(self.hdmi Ports)+' '+datetime,utcnow().st
rftime('%Y med H&M\S_*) [-2]+.jpg' client machine
imgcrop
-self.compImagePath+r'crop
Img_+datetime.utcnow().strftime('4Y\m\d_H&M÷S_
f')[:-21+.jpg' #bangalore machine print (imgcrop)
pixels))
minimum
print (self.capturedImage)
gray = cv2.imread(self.capturedImage) if gray is not None:
gray = cv2.resize (gray, (960, 540)) graylyl:y2, x1:x2]
roi
cv2.imshow("captured", gray) cv2.waitKey (2000)
cv2.destroyWindow("captured") cv2.imwrite (imgcrop, roi) img1 cv2.imread(imgcrop)
cv2.imshow("cropped", img1) cv2.waitKey (2000)
cv2.destroyWindow ("cropped") print (imgcrop)
if self.method == 'Image':
#The method used for image comparison
methods['cv2.TM_SQDIFF_NORMED]
capture the start time before image comparison start_time datetime.now()
# read the captured image
image cv2.imread(imgcrop, 0)
# read the reference/template image
template cv2.imread(self.reference Image, 0)
#print (template)
Define the size (( of width w pixels and height h
w, h template.shape[::-11
for meth in methods:
method= eval (meth)
print (image)
# Apply template Matching
res cv2.matchTemplate (image, template, method)
min_val, max_val, min_loc, max_loc= cv2.minMaxLoc (res) # If the method is TM SQDIFF or TM SQDIFF_NORMED, take
if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: top_left min_loc
first_pass_certainty (1 min_val) end_time = datetime.now()
print(('Duration for Image comparision :
{}'.format (end_time - start_time)))
first_pass_certainty)
print ("method used", meth)
print("Pass Criteria = "+str(threshold_value)) print ("Max Value Achieved = ",
# Check with Threshold value
﻿

if first_pass_certainty > threshold_value:
print ("Test Pass")
else:
ret_val = "Pass"
print ("Test Fail") ret val "Fail"
return ret_val
elif self.method Text':
ret_val = self.compareText (imgcrop) return ret_val
if gray is None:
raise ValueError("Please check the captured image in the path
is proper!!!")
def capture_image (self, captured Image):
This function will capture the Image of the STB screen using Capture card.
During the True condition this will use the click and crop method where the user have to
click and crop on the image to select the area of interest.
During False condition it will make use of the coordinates that are stored during the True condition and
gets that image.
:param captured Image: The Captured image will be stored with this given image name.
:return: Will return the Captured Image
print ("capture")
if self.autocal is True:
print("inside capture")
print ("cap_image"
cap_image- self.get_image (capturedImage)
cap_image)
return cap_image
else:
self.timeStamp
self.imageName
time.strftime("%Y med_&H M8S", time.gmtime()) capturedImage+' '+self.timestamp
print (cap_image)
cap_image self.get_image (self.imageName)
return cap_image
def compare_image (self, reference Image, captured Image,
threshold_value=0.8):
www
This function will compare whether the captured image from the Capture card and the given
reference image are the same.
The parameters threshold value can be modified as per the required accuracy level.
:param reference Image: This is the expected reference image :param capturedImage: This is the live capture image of STB from Capture card.
:param threshold_value: This value ranges from 0.1 to 1.0 :return: will return Pass or Fail based on the calibration done.
www
print ("compare")
print (self.autocal)
print ("threshold_value:", threshold_value)
if self.autocal is True:
self.result = self.auto_calibration (captured Image)
﻿

S)
else:
print ("compare false") print (referenceImage) print (capturedImage) img_comp_res = list() count 0
for s in capturedImage:
threshold_value)
print ("Doing comparison between :"+ referenceImage,
print (referenceImage)
self.resultself.isImageFound (reference Image, 5,
if int (self.hdmi Ports [count]) -- 0: self.porto.append(self.result) self.overall_port_0.append(self.result)
if int (self.hdmi Forts [count])==1: self.portl.append(self.result)
self.overall port_1.append(self.result) if int (self.hdmi Ports[count]) == 2: self.port2.append(self.result) self.overall_port_2.append(self.result)
if int (self.hdmi Ports[count])-3:
self.port3.append(self.result)
self.overall port_3.append(self.result)
count + 1
img_comp_res.append(self.result)
print("list::", img_comp_res)
for i in img_comp_res:
print ("inside for loop", 1)
if i'Fail':
self.result = "Fail"
return self.result
def find image (self, image, crop image, threshold_value 0.8):
This function checks for the reference given image is available in the big captured image
The parameters threshold value can be modified as per the required accuracy level.
:param image: Big image
:param crop image: reference image to be found on the big image param threshold_value: value ranges from 0.1 to 1.0
return: Will return Pass or Fail
www
print ("inside find image")
img_comp_res = list()
print (image)
count=0
for s in image:
print (s)
res self.image_search(s, crop image, threshold_value) if int (self.hdmi Ports [count]) == 0:
self.porto.append(res) self.overall_port_0.append(res)
if int(self.hdmi Ports [count])
-=1:
self.portl.append(res) self.overall_port_1.append(res)
if int(self.hdmi Ports [count]) -- 2: self.port2.append(res)
self.overall_port_2.append(res)
if int (self.hdmi Ports [count]) == 3:
﻿

self.port3.append(res)
self.overall port_3.append(res)
count + 1
img_comp_res.append(res)
print (self.porto, self.portl, self.port2, self.port3) print("list::", img_comp_res)
for i in img_comp_res:
if i'Fail:
res = "Fail"
return res
def image_search(self, main_img, crop img, threshold_value):
This function is called from
find_image keyword.
self. Image
self.compImagePath+main_img
print ("image:", self.Image)
print ("crop_img", crop_img)
print ("Finding crop_img", crop img," in this screen=",
self.Image)
img_rgb = cv2.imread(self.Image)
if img_rgb is not None:
img_rgb
img_gray
=
=
cv2.resize(img_rgb, (960, 540))
cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template cv2.imread(crop_img, 0)
print (template)
w, h= template.shape[::-1]
res = cv2.matchTemplate (img_gray, template,
cv2.TM_CCOEFF_NORMED)
threshold threshold_value
loc= np. where (res >= threshold)
print (loc[0])
if len(loc[0]) == 0:
else:
return "Fail"
return "Pass"
if img_rgb is None:
the path")
list.
raise ValueError ("Please check the given image is available in
def verify_image_data(self, imageA, crop_image_a, day_list):
This function is to check for the day whether it presents in given
www
print ("inside find image")
img_comp_res = list()
print (imageA)
count=0
for s in imageA:
print (s)
res = self.day (s, crop_image_a, day_list) if int (self.hdmi Ports [count])== 0:
self.port0.append (res)
self.overall_port_0.append(res)
if int (self.hdmi Ports [count]) == 1: self.portl.append(res) self.overall_port_1.append(res)
if int (self.hdmi Ports [count]) == 2: self.port2.append(res)
﻿

self.overal1_port_2.append(res)
if int(self.hdmi Ports [count]) = 3: self.port3.append (res)
self.overall_port_3.append(res)
count += 1
img_comp_res.append(res)
print ("list::", img_comp_res)
for i in img_comp_res:
print ("inside for loop", i)
if i'Fail':
res "Fail"
return res
def day (self, imageA, crop_image_a, day_list):
This function is called from verify_image_data keyword.
"""
curr_path = self.directory
database = os.path.join(curr_path, "TestScripts/LIB/DB/refImage.db") print (database)
conn = sqlite3.connect (database)
curs = conn.cursor()
self.imageName = os.path.basename (crop_image_a)
query3 = 'select xy_coordinates from + self.table_name + ' where imgName = " + self.imageName +
'";'
print (query3)
curs.execute(query3)
xy_coordinates curs.fetchone()
print(("print (xy_coordinates", xy_coordinates))
xy_coordinates
=
xy_coordinates [0]
print (xy_coordinates)
print ((eval (xy_coordinates))) xy_coordinates eval (xy_coordinates) print ((type (xy_coordinates)))
x1 = int (xy_coordinates [0][0]) yl int (xy_coordinates [0] [1])
x2
y2
M
=
img_a
int (xy_coordinates [1][0])
int (xy_coordinates [1][1])
=
imageA
print ("img_a", img_a)
img_crop = os.path.join(self.compImagePath, img_a)
print (img_crop)
gray = cv2.imread(img_crop)
if gray is not None:
print (gray)
grayl= cv2.resize (gray, (960, 540))
roil grayl [yl: y2, x1:x2]
print(('After Resize Capture Image: ', roil))
cv2.imshow("cropped", roil)
cv2.waitKey (3000)
cv2.destroyWindow ("cropped")
roil = cv2.cvtColor (roil, cv2.COLOR_BGR2GRAY)
filename = "{}.jpg".format("temp")
﻿

cv2.imwrite(filename, roil)
filename cv2. Imread (filename)
filename cv2.resize (filename, None, Ex-2, ty-2,
interpolation-cv2. INTER CUBIC)
thresh cv2.threshold (filename, 83, 255,
cv2.THRESH BINARY_INV) [1]
text pytesseract.image_to_string (thresh, lang-'eng')
text("".join(text.split())
if text in day_list:
print('Present'). return 'Pass'
else:
print ("Not present") return 'Fail'
if gray is None:
the path")
raise ValueError("Please check the given image is available in
def verify_time_format (self, imageA, crop_image_a, time_format):
This verifies the extracted time from the screen matches the given time format.
print ("inside find image")
img_comp_res = list()
print (imageA)
count=0
for s in imageA:
print (s)
res = self.time (s, crop_image_a, time_format) if int (self.hdmi Ports [count])
self.port0.append(res)
0:
self.overall_port_0.append(res)
if int(self.hdmi Ports [count]) == 1: self.portl.append(res) self.overall_port_1.append(res)
if int(self.hdmi Ports [count]) == 2: self.port2.append(res)
self.overall_port_2.append(res)
if int(self.hdmi Ports [count])
self.port3.append(res)
3:
self.overall_port_3.append(res)
count += 1
img_comp_res. append(res)
print ("list::", img_comp_res)
for i in img_comp_res:
print ("inside for loop", i) if i'Fail':
res "Fail"
return res
def time (self, image_a, crop_image_a, time_format):
This verifies the extracted time from the screen matches the giv time format.
curr_path = self.directory
database = os.path.join(curr_path, "TestScripts/LIB/DB/refImage.db")
﻿

print (database)
conn
curs
sqlite3.connect (database)
conn.cursor()
self.imageName = os.path.basename (crop_image_al
query3 select xy_coordinates from self.table_name + imgName "self. imagellame + ";"
print (query3)
curs.execute(query3)
xy_coordinates curs.fetchone ()
print(("print (xy_coordinates", xy_coordinates))
xy_coordinates
xy_coordinates[0]
print (xy_coordinates)
print ((eval (xy_coordinates)))
xy_coordinates eval (xy_coordinates) print((type (xy_coordinates)))
x1
yl
x2
int (xy_coordinates[0][0])
int (xy_coordinates[0][1])
int (xy_coordinates [1][0])
y2int (xy_coordinates [1][1]) img_a-image_a
print ("img_a", img_a)
img_a
os.path.join(self.compImagePath, img_a)
print (img_a)
gray cv2.imread(img_a)
if gray is not None:
print (gray)
grayl cv2.resize(gray, (960, 540))
roil grayllyl: y2, x1:x2]
print(('After Resize Capture Image:', roil))
cv2.imshow("cropped", roil)
cv2.waitKey (3000)
cv2.destroyWindow("cropped")
filename
"().jpg".format("temp")
cv2.imwrite(filename, roil)
filename cv2.imread(filename)
filename = cv2.resize(filename, None, Ex-2, Ey-2,
interpolation-cv2.INTER CUBIC)
thresh cv2.threshold (filename, 83, 255,
cv2.THRESH BINARY_INV) [1]
text-pytesseract.image_to_string (thresh, lang="eng') print("text", text)
text("".join(text.split()))
print (len (text), len (time_format))
try:
time.strptime (text, time format) return 'Pass'
except ValueError:
return 'Fail'
if gray is None:
the path")
where
raise ValueError("Please check the given image is available in
def extract_image_text(self, image_a, crop_image_a):
    ﻿

    This
    will
    extract
    text
    from the cropped
    image.
    print("inside extract text image")
    ing
    comp
    realist()
    print(image_al
          for a in image
    at
    print(s)
    res
    self.extract
    text(s, crop_image_al
    img_comp_res.append(ren)
    print("list::", img_comp_res)
    return ing
    comp_res

    def extract text(self, image_a, crop

    image_4):
    www
    This
    function is called
    from extract_image_text keyword.
    www
    curr_path
    database
    self.directory
    os.path.join(curr_path,
                 "TestScripts/LIB/DB/refImage.db")
    print(database)
    conn
    sqlite3.connect(database)
    curs
    conn.cursor()
    self.imageName
    os.path.basename(crop_image_a)
    query3
    'select xyCoordinates from self.table_name + imgName" + self.imageName+"";
    print(query3)
    curs.execute(query3)
    xy_coordinates
    curs.fetchone()
    print(("print (xy_coordinates", xy_coordinates)} xy_coordinates
    xy_coordinates[0]
    print(xy_coordinates)
    print((eval(xy_coordinates)))
    xy_coordinates
    eval(xy_coordinates)
    print((type(xy_coordinates)))
    x1
    yl
    x2
    y2
    int(xy_coordinates[0][0])
    int(xy_coordinates[0][1])
    int(xy_coordinates[1][0])
    int(xy_coordinates[1][1])
    img_a
    image_a
    print("img_a", img_a)
    img_crop = os.path.join(self.compImagePath, img_a)
    print(img_crop)
    gray
    cv2.imread(img_crop)
    if gray is not None:
        print(gray)
    gray1 = cv2.resize(gray, (960, 540))
    roil
    grayl[yl: y2, x1:x2]
    print(('After Resize CaptureImage:', roil))
    cv2.imshow("cropped", roil)
    cv2.waitKey(3000)
    cv2.destroyWindow("cropped")
    roil = cv2.cvtColor(roil, cv2.COLOR_BGR2GRAY)
    filename = "().jpg".format("temp")
    cv2.imwrite(filename, roil)
    filename
    cv2.imread(filename)
    filename = cv2.resize(filename, None, fx - 2, £y = 2,
    interpolation - cv2.INTER_CUBIC)
    thresh = cv2.threshold(filename, 83, 255,
                           cv2.THRESH_BINARY_INV)[1]
    ﻿

    text
    pytesseract.image_to_string(thresh, lang - eng
    ') text("".join(text.split()))
    return text
    if gray is None:
        the
        path
        ")
    raise ValueError("Please check the given image is available in

    def fetch_image_text(self, image_a, crop_image_a):
        This
        function
        will
        extract
        the
        text
        from given cropped
        image.

    print("inside fetch image")
    img_comp_res = list()
    print(image_a)
    for s in image_a:
        print(s)
    res
    self.image_text(s, crop_image_a)
    img_comp_res.append(res)
    print("list::", img_comp_res)
    return img_comp_res

    def image text(self, image_a, crop_image_a):

    This
    fnction is called
    from fetch_image_text keyword.
    curr_path = self.directory
    database = os.path.join(curr_path, "TestScripts/LIB/DB/refImage.db")
    print(database)
    imgName
    conn =
    sqlite3.connect(database)
    curs
    conn.cursor()
    self.imageName = os.path.basename(crop_image_a)
    query3
    'select xyCoordinates from self.table_name + ⚫ where "self.imageName+!";
    print(query3)
    curs.execute(query)
    xy_coordinates = curs.fetchone().
    print((" (xy_coordinates", xy_coordinates))
    xy_coordinates = xy_coordinates[0]
    print(xy_coordinates)
    print((eval(xy_coordinates)))
    xy_coordinates
    eval(xy_coordinates)
    print((type(xy_coordinates)))
    x1
    yl
    x2
    y2
    =
    int(xy_coordinates[0][0])
    int(xy_coordinates[0][1])
    int(xy_coordinates[1][0])
    int(xy_coordinates[1][1])
    =
    img_a
    image_a
    print("img_a", img_a)
    img_crop = os.path.join(self.compImagePath, img_a)
    print(img_crop)
    gray
    cv2.imread(img_crop)
    if gray is not None:
        print(gray)
    grayl = cv2.resize(gray, (960, 540))
    roil
    grayl[yl: y2, x1:x2]
    print(('After Resize Capture Image:', roil))
    ﻿

    cv2.imshow("cropped", roil)
    cv2.waitKey(3000)
    cv2.destroyWindow("cropped")
    roil
    cv2.cvtColor(roll, cv2.COLOR_BGR2GRAY)
    filename
    "1).jpg".format("temp")
    cv2.imwrite(filename, roil)
    filename
    cv2.imread(filename)
    filename = cv2.resize(filename, None, fx - 2, fy - 2,
                          interpolation - cv2.INTER
    CUBIC)
    text
    pytesseract.image_to_string(filename, lang="eng') text- ("".join(text.split()))
    return text
    if gray is None:
        the
        path
        ")
    raise ValueError("Please check the given image is available in

    def pass fail_count(self):

    This
    will
    print
    the
    total
    number
    of
    pass and fail
    count
    of
    TestCases
    for each port in the log file when called.
    print("TOTAL PASS/FAIL COUNT ON PORTO FOR TESTCASE: ", len(self.port0))
    print("TOTAL PASS/FAIL COUNT ON PORTI FOR TESTCASE:",
          len(self.port1))
    print("TOTAL PASS/FAIL COUNT ON PORT2 FOR TESTCASE:",
          len(self.port2))
    print("TOTAL PASS/FAIL COUNT ON PORT3 FOR TESTCASE:", len(self.port3))
    print("###
    COUNT
    COUNT
    COUNT
    COUNT
    PORTO: PASS / FAIL
    print("PORTO_PASS_COUNT: ", self.port0.count('Pass'))
    print("PORTO_FAIL_COUNT:", self.port0.count('Fail'))
    print("###
    PORTI: PASS / FAIL
    print("PORT1 PASS_COUNT:", self.port1.count('Pass'))
    print("PORT1 FAIL_COUNT:", self.port1.count('Fail'))
    print("#s
    PORT2: PASS / FAIL
    print("PORT2_PASS_COUNT:", self.port2.count('Pass'))
    print("PORT2_FAIL_COUNT:", self.port2.count('Fail'))
    print("##
    PORT3: PASS / FAIL
    print("PORT3_PASS_COUNT:", self.port3.count('Pass'))
    print("PORT3 FAIL COUNT: ", self.port3.count('Fail'))

    def count(self):
        www

    This
    function is called
    from
    pass
    fail_count
    function.
    www
    self.port0 = list()
    self.portl = list()
    self.port2 = list()
    self.port3 = list()

    def overall_pass_fail_count(self):
        ﻿

        This
        will
        print
        the
        over
        all
        pass and fall
        count
        of
        TestCases
        for each port in the log file when called.
        print("TOTAL PASS/FAIL COUNT ON PORTO FOR ALL TESTCASE", len(self.overall_port_01)
        print("TOTAL PASS/FAIL COUNT ON PORTI FOR ALL TESTCASE: ", len(self.overall_port_1))
        print("TOTAL PASS/FAIL COUNT ON PORT2 FOR ALL TESTCASE:", len(self.overall_port_2))
        print("TOTAL PASS/FAIL COUNT ON PORT3 FOR ALL TESTCASE:", len(self.overall_port_3))
        print(" ***** PORTO: PASS/FAIL
        COUNT
        COUNT
        COUNT
        COUNT
        print("PORTO PASS_COUNT: ", self.overall_port_0.count('Pass'))
        print("PORTO_FAIL_COUNT:", self.overall
        port
        0.
        count('Fail')) print("## PORTI: PASS/FAIL
        print("PORT1_PASS_COUNT: ", self.overall_port_1.count('Pass'))
        print("PORT1 FAIL COUNT:", self.overall_port_1.count('Fail'))
        print("###
        PORT2: PASS / FAIL
        print("PORT2_PASS_COUNT: ", self.overall_port_2.count('Pass'))
        print("PORT2_FAIL_COUNT: ", self.overall
        port
        2.
        count('Fail')) print("### PORT3: PASS/FAIL
        print("PORT3_PASS_COUNT: ", self.overall_port_3.count('Pass'))
        print("PORT3_FAIL_COUNT:", self.overall
        port_3.count('Fail'))

        def db_check(self, file_name):
            This
            function
            will
            check
            for all the reference Images captured are stored in the Database file.:param
            file_name: Will
            take
            excel
            sheet
            name
            with reference image names as input.:return: Will
            return the
            reference
            image
            name
            which is not stored in the
            Database
            file,

        """
        df = pd.read_excel (file_name, sheet_name-0) can also index sheet by name or fetch all sheets
        reference_images de l'Image_Name'].tolist()
        print (reference_images)
        conn =
        sqlite3.connect (os.getcwd () +r'/TestScripts/LIB/DB/refImage.db')
        c = conn.cursor ()
        for item in reference_images:
        item_str = "'"+item+".jpg"+"*"
        query=
        f'SELECT EXISTS (SELECT xyCoordinates FROM STB WHERE imgName = (item str) LIMIT 1)'
        db check
        c.execute(query).fetchall()
        if db check[0][0] = 0:
        raise ValueError (f'Make sure the image (item_str) captured
        in True condition')
        else:
        pass
        def set_ports (self):
        ﻿

www
Will set the four Ports ready to receive the input video signal.
www
os.system('v412-ctl --device /dev/video0 --set-input-1') os.system (v412-ctl --device /dev/videol --set-input-1') os.system ('v412-ctl --device /dev/video2 --set-input-1') os.system('v412-ctl --device /dev/video3 --set-input-1')
def clear_ports (self):
signals.
Will Clear all the Ports to make it available to receive input
$2) | xargs kill -9
os.system("lsof | grep '/dev/video* | grep -v grep | awk '{print >"+os.environ['HOME']+"/Cogmation/logs/Cogmation_logs.log 2>&1")
#ADB COMMANDS
def adb_connect (self, deviceip):
file os.getcwd () +
"/TestScripts/LIB/PYTHON/Validation.txt"
cmd="adb connect "+deviceip+" >"+file
os.popen (cmd)
time.sleep (3)
fp-open (file, "r")
result-fp.read()
result result[:-1] fp.close()
return result
def installingapk (apk):
file= os.getcwd () +
"/TestScripts/LIB/PYTHON/Validation.txt"
cmd="adb -s "+self.deviceip+" install -d "+apk+" >"+file
print (cmd)
os.popen (cmd)
time.sleep (60)
fp-open (file, "r")
result-fp.read()
print (result)
result result[:-1]
fp.close()
return result
def input_keyevent (self, signal):
cmd ="adb -s "+self.deviceip+" shell input keyevent "+signal print (cmd)
os.popen (cmd)
def Dump_Logcat (self, filename):
subfolder = time.strftime ("%d-8m-8Y")
curr_dir = os.getcwd ()
sub_path
"/TestScripts/ADB_LOGS/"+subfolder+"/"
if not os.path.exists(curr_dir + sub_path):
os.mkdir (curr_dir + sub_path)
filepath = curr_dir + sub_path +filename+"_Logs.txt"
cmd = "adb -s "+self.deviceip+" shell logcat -d>"+filepath os.popen (cmd)
return filepath
def Clear_Logcat (self):
cmd="adb -s "+self.deviceip+" shell logcat -c" os.popen (cmd)
﻿

def Input Text (self, text):
cmd"adb-s
os.popen (cmd)
self.deviceipt shell input text text
def compare screen (self, img1, img2):
This function compares two images param img1: Captured full Screen image :paran ing2: Captured full Screen Image
: return: return Pass if both images are same return Fail if both images are different
img1))
hash0 hashi
img2))
hashes.
imagehash.average_hash (Image.open(self.compImagePath +
imagehash.average_hash (Image.open(self.compImagePath +
cutoff = 3 # maximum bits that could be different between the
if hash0-hashi < cutoff:
return "Pass"
else:
return "Fail"
#STB1-STB (os.getcwd())
#img-STB1.capture_image ("Put_Device_To_Sleep")
#result = STB1.compare_image ("Put_Device_To_Sleep.jpg",ing, 0.8) #print (result)
#result-
STB1.fetch_image_text (img, "/home/user/DT_STB_Automation/IMAGES/STB/Referenc e_Images/sample.jpg")
# print (result)
# result -
STB1.extract_image_text (ing, "/home/user/DT STB Automation/IMAGES/STB/Refere nce_Images/sample.jpg")
#print (result)
#result =
STB1.find_image (img, "/home/user/DT_STB_Automation/IMAGES/STB/Reference_Imag es/Sample.jpg")
#print (result)
#result-STB1.adb_connect('192.168.1.104:5555")
# print (result)
# result-STB1.input_keyevent ('3')
#print (result)
#result-STB1. Dump_Logcat ("Setting-in-the-application-
login_DT Setting InApp_TC_01")
#print (result)
#result-STB1.compare_screen("/home/user/JC_1_Agent_1/JC_1_Agent_1_DUT_2/wor
kspace/DT/TestScripts/IMAGES/STB/Screen1.jpg", "/home/user/JC_1_Agent_1/JC_1
Agent_1_DUT_2/workspace/DT/TestScripts/IMAGES/STB/Screen2.jpg")
#print (result)









