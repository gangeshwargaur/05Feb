
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
﻿

#TeardownStatusTC. Status
CAPTURE REFERENCE IMAGE
Siexecution sai Fall Completed
[Arguments] Sireterence image
Bulitin.sleep 1
stthreshold valu)-0.80
311mg) STB.capture image testerence image)
$Result) STB.compare image intereson ini.jpg threshold value-threshold wines
[Return] Result)
VERIFY IMAGE
(Arguments) $(reference_image) $(threshold value)-0.80 Builtin.sleep 1
(Img) STB.capture image reference Image)
$Result! STB.compare image Streference image.jpg (5) threshold value-51threshold value)
[Return] $Result)
VERIFY IMAGE ON SCREEN
(Arguments) $(reference_image) $(threshold_value)-0.80
5(autocal) STB.Scheduling
BuiltIn.sleep
1
$(Img) STB.capture image $(Result) Run Keyword If
$[Img]
reference image
(autocal)-'False STB.find_image
$(EXECDIR)/TestScripts/IMAGES/STB/Reference Images/5 reference_image).jpg
threshold value-S(threshold_value]
[return] $(Result)
FETCH TEXT FROM SCREEN
[Arguments] $(reference_image) $(autocal) STB.Scheduling
BuiltIn.sleep 1
$(Img) STB.capture image
$(Result) Run Keyword If
$(reference_image 'S(autocall 'False"
STB.fetch_image_text $1 Img
SEXECDIR)/TestScripts/IMAGES/STB/Reference_Images/51reference_image).jpg
[return] $Result[0])
EXTRACT TEXT FROM SCREEN
[Arguments] $(reference_image)
$(autocal) STB.Scheduling
BuiltIn.sleep
$(Img] STB.capture image $reference_image) ${Result) Run Keyword If '$(autocal) - 'False" STB.extract_image_text $[Img)
$ EXECDIR)/TestScripts/IMAGES/STB/Reference_Images/$(reference_image).jpg
[return] $Result[0])
CAPTURE PAGE
[Arguments]
$(reference_image)
Builtin.sleep 1
$(Img) STB.capture image $(reference_image) [return] $(Img[0])
COMPARE SCREEN
[Arguments] $imgl) $(img2)
Builtin.sleep 1
$(Result) STB.compare screen $(img1) $(img2) [Return] $(Result)
{Return}   ${Result}
﻿

ADB CONNECT
[Argumental $(devicelp)
$(Result) STB. adb connect
Run Keyword If '(Result
devicelp)
(Result)-- already connected to IDEVICE IP LOG Device Is connected to IDEVICE IP or Connected Successfully console-yes
ELSE FATAL ERROR (Result)
DUMP LOGCAT
[Arguments] $(file)
#Log To Console Dumping Logs in $(file).txt $(filename) STB. Dump Logcat $[file]
Log To Console Dumped Logs To S(filename)
CLEAR LOGCAT
Log To Console Clearing Logs
STB.Clear Logcat
CLICK
(Arguments]
$(KeySignal)
STB. Input Keyevent $($(KeySignal}} Sleep is
GO TO HOME PAGE
CLICK HOME
Log To Console Verifying Home Page!!!
$ (Result)
VERIFY IMAGE MenuBar
[Return] $ (Result]
ENTER PIN
[Arguments] $(img) $(pin)
$(Result) VERIFY IMAGE $(img)
Run Keyword If '$(Result)'= 'Pass' INPUT TEXT $(pin)
CHANGE PIN
CLICK OK
$(Result) VERIFY IMAGE Age RatingPin Run Keyword If '$(Result)''Pass' Sleep 2s
INPUT TEXT $(NEW PIN)
$(Result) LAUNCHING SPECIFIC OPTION FROM SETTINGS SCREEN
$ SETTINGS IN THE TV APPLICATION
Run keyword If $(Result) 'Pass' Log To Console Setting Screen. Is Launched
ELSE Fail Setting Screen Is Not Launched
$ [Result) NAVIGATING TO PARTICULAR OPTION IN SELECTED SETTINGS OPTIONS $IS SECURITY)
Run Keyword If '${Result)''Pass' Log To Console Security page is displayed
ELSE Fail Security page is not displayed
${Result) NAVIGATING TO PARTICULAR OPTION IN SELECTED SETTINGS OPTIONS $1SECURITY CHANGEPIN}
Run Keyword If '$(Result)' == 'Pass' INPUT TEXT $(NEW PIN ENTER PIN New Pinimg $(OLD_PIN)
ENTER PIN
Sleep 1s
Confirm Pin $(OLD PIN
$(Result) VERIFY IMAGE Security Options
Run Keyword If '$ (Result)' == 'Pass' Log To Console Pin Changed ... ELSE Fail Pin Is Not Changed
${Result) NAVIGATING TO PARTICULAR OPTION IN SELECTED SETTINGS OPTIONS
﻿

SIGN IN TO GOOGLE ACCOUNT
[Arguments)
CLICK sleep
OK 2
$(mail_id) (mail_password)
Log To Console Sign In Screen
$(Result) VERIFY IMAGE Sign In
Run Keyword If '$Result)''Pass
Is Displayed
ELSE Fail Sign In Screen Is Not Displayed CLICK OK
sleep 4
$[Result) VERIFY IMAGE Use_Your_Google_Account
Run Keyword If '$(Result) -- 'Pass' Log To Console Enter Mail Id Screen Is Displayed
ELSE Fail
Enter Mail Id Screen Is Not Displayed
INPUT TEXT $(MAIL ID)
Sleep 23
CLICK BACK
Repeat Keyword 2 times CLICK DOWN
CLICK RIGHT
CLICK OK
sleep 4
$(Result) VERIFY IMAGE Show Password
Run Keyword If '$(Result) 'Pass' Log To Console Enter Password Screen Is Displayed
ELSE Fail Enter Password Screen Is Not Displayed
INPUT TEXT $(MAIL PASSWORD
Sleep 2s
CLICK BACK
Repeat Keyword 2 times CLICK DOWN
CLICK RIGHT
CLICK OK
sleep 6
$(Account_Info)
Run Keyword If
FETCH TEXT FROM SCREEN No Account_Image
$(Account Info)'
Successfully Signed In To "$ (MAIL_ID}"
'S (MAIL ID) Log To Console
... ELSE FAIL Not Able To Sign In "$(MAIL_ID)"
NAVIGATE TO FAVOURITES IN HOME SCREEN
GO TO HOME PAGE
Repeat Keyword 3 CLICK DOWN
$ (Result) VERIFY IMAGE
[Return] $(Result)
VIEW ALL FAVOURITE
CLICK HOME
Favourite_Home
Repeat Keyword 3 CLICK DOWN
CLICK LEFT
$(Result) VERIFY IMAGE Favourites Viewall
Run Keyword If
[Return] Pass
'$(Result). == 'Pass' CLICK OK
NAVIGATE TO NOW ON IN HOME PAGE
$(Result) GO TO HOME PAGE
Run keyword If '$(Result)' -- 'Pass' Log To Console Home Screen Is Launched
ELSE Fail Home Screen Is Not Launched
Repeat Keyword 2 CLICK DOWN
Log To Console Verifying Now ON In Home Page!!! $(Result) VERIFY IMAGE NowOn_Home
[Return] ${Result)
﻿

AND Return From Keyword
Log to Console Logging To Magenta TV!!!
CLICK OK
${Result) VERIFY IMAGE Username
Run Keyword If
Not Highlighted
0.96
'S(Result)!- 'Pass' Fail "Enter username" Field Is
"Enter username" Field Is Highlighted!!!
$USERNAME]
Log to Console INPUT TEXT Sleep 28
CLICK BACK
CLICK DOWN
$(Result) VERIFY IMAGE Password
Run Keyword If
Not Highlighted
Log to Console INPUT TEXT Sleep 25
CLICK BACK
'$[Result] - 'Pass Fail "Enter Password" Field Is
"Enter Password" Field Is Highlighted!!!
$[PASSWORD]
CLICK DOWN
CLICK OK
Sleep 3s
$(Result) VERIFY IMAGE (SETTINGS IN THE TV APPLICATION['Image2']} Run Keyword If '$(Result)--'Pass' Log to Console Successfully
Login To Magenta TV
ELSE Fail Not Login To Magenta TV
LOGOUT FROM MAGENTA TV
$(Result) LAUNCHING SPECIFIC OPTION FROM SETTINGS SCREEN $(SETTINGS IN THE TV APPLICATION
Run Keyword If $(Result) 'Pass' Log To Console Settings Panel Is Launched
ELSE AND $(Result)
$(S_LOGOUT
Run keywords Log To Console Already logged out Return From keyword
NAVIGATING TO PARTICULAR OPTION IN SELECTED SETTINGS OPTIONS
Run Keyword If '$(Result' --
Confirmation Popup Is Displayed
'Pass Log To Console Logout
ELSE Fail Logout Confirmation Popup Is Not Displayed
Log To Console Selectiing Cancel Option!!!
CLICK LEFT
CLICK OK
$(Result) VERIFY IMAGE Logout
Run Keyword If 'S(Result) -- 'Pass' Log to Console Logout Confirmation Popup Is Dismissed
#
ELSE Fail Logout Confirmation Popup Is Not Dismissed Log To Console Logout from Magenta TV
Repeat Keyword 3 times
CLICK OK
Sleep 25
$(Result) VERIFY IMAGE Logging Out
Run Keyword If '$Result) -- 'Pass' Log To Console Logout Confirmation Popup Is Displayed
ELSE Fail
CLICK OK
Sleep 2s
$(Result) VERIFY IMAGE LoginPage
Run Keyword If '$(Result)'
Logout From Magenta TV
'Pass' Log to Console Successfully
... ELSE Fail Magenta TV Is Still Login
CLICK HOME
﻿

SECURITY AGERATTRUY
Run Keyword If 'SERI
-Pass INPUT TEXT OLD PIRE
$(Result) VERIFY IMAGE Age RatingEnabled Run Keyword It
Successfully Changed
Result)-Pass Log To Console Pin 1s
... ELSE Fall Pin to Not Changed
NAVIGATE TO ANY OPTION ON MENU
(Arguments)
CLICK GUIDE
$(menu_option)
$(Result) GO TO HOME PAGE
Run keyword If 'ResultPass Log To Console Home Screen Is Launched
ELSE Fall
Log To Console
Repeat Keyword
Home Screen Is Not Launched
Navigating To $(menu_option('Option!!! Simenu_option('No_of_Times_Right'
CLICK RIGHT
Repeat Keyword Simenu option (No of Times Left'l CLICK LEFT CLICK OK
$(Result)
VERIFY IMAGE $menu_option("Image") [Return] $Result)
LAUNCHING SPECIFIC OPTION FROM SETTINGS SCREEN
[Documentation] To Navigate specific settings option (General device settings/My Tv etc)
Arguments should be $(GENERAL_DEVICE_SETTINGS)/(MY TV etc mentioned in DT.yaml file
[Arguments] $(settings_option)
$(Result) NAVIGATE TO ANY OPTION ON MENU SISETTINGS_ICON
Run Keyword If 'S/Result) 'Pass' Log to Console Navigated To Settings Screen
ELSE Fail Settings Screen Is Not Launched
Log To Console Navigating To 'Sisettings_option["Option"]]'!!! Repeat Keyword $(settings_option('No_Of_Times_Down'11 CLICK DOWN Repeat Keyword Sisettings_option('No_Of_Times_Right 11 CLICK RIGHT $(Result) VERIFY IMAGE $(settings_option!'Imagel'])
Run Keyword If 'S(Result)' == 'Pass'
CLICK OK
ELSE Fail $(settings_option("Option']) Option Is Not Highlighted ${Result) VERIFY IMAGE $settings option['Image2'11
[Return] $Result)
NAVIGATING TO PARTICULAR OPTION IN SELECTED SETTINGS OPTIONS
[Documentation] To Navigate particular option in selected settings option (Eg: In General Settings/Device Preference/Settings) Arguments should be defined in yaml file as $IGS_DEVICE_PREFERENCES)/S(DP_REBOOT}/${S_LOGOUT)
[Arguments]
$(sub_option)
Log To Console Selecting $isub_option('Option'])!!!
Repeat Keyword $(sub_option('No_Of_Times_Down'11 CLICK DOWN CLICK OK
${Result) VERIFY IMAGE
[Return] $(Result)
LOGIN TO MAGENTA TV
Log To Console Login
$sub_option("Reference_Image'1}
LAUNCHING SPECIFIC OPTION FROM SETTINGS SCREEN
$(SETTINGS IN THE TV APPLICATION)
Sleep 2s
$(Result) VERIFY IMAGE Login Page
Run Keyword If 'S(Result) - 'Pass' Run Keywords Log To Console
Already Login To Magenta TV
﻿

NAVIGATE BACK TO GENERAL SETTINGS
FOR $(INDEX) IN RANGE 0 20
END
$(Result) VERIFY IMAGE GDSettings Option_Highlight Run Keyword If '5(Result) 'Pass' Exit For Loop ELSE CLICK BACK
CHANGE SCREENSAVER OPTION TO TURNSCREENOFF/BACKDROP/COLORS ON SCREENSAVER SCREEN
[Arguments] $tas_option)
CLICK OK
Log To Console Changing Screen Saver Option To
$(an option['Option'11!!!
Repeat Keyword $iss_option['No_of_Times_Down' CLICK DOWN CLICK OK
Sleep la
$(selected option) EXTRACT TEXT FROM SCREEN SS Highlighted Option Run Keyword If '$(selected option) - To Console 'Siss_option('option'11' ScreenSaver Option Is Selected Siss_option['option'11' Log ELSE FAIL $iss_option['option'11' Screensaver option Is Not
Selected
CHANGE SCREEN SAVER WHEN TO START OPTION TO 5M/15M/30M/1H/2H ON SCREENSAVER SCREEN
[Arguments) $(time)
CLICK DOWN
CLICK OK
$(Result) VERIFY IMAGE When_to_start
Run Keyword If 'S(Result)''Pass' Log To Console Navigated To When To Start Screen
ELSE Fail Not Navigated To When To Start Screen
Repeat Keyword
$(time['No_Of_Times_Down'11
Repeat Keyword 2 times CLICK OK
CLICK DOWN
0.9
$(Result) VERIFY IMAGE $(time['Reference Image'11
Run Keyword If '$(Result)''Pass' Log To Console Screen Saver
Time Is Changed To $(time['Waiting Time']}
ELSE Fall Screen Saver Time Is Not Changed To
$(time('Waiting Time'])
CLICK BACK
CHANGE SCREEN SAVER PUT DEVICE TO SLEEP MODE OPTION TO
30M/1H/3H/6H/12H/Never
[Arguments] $(time)
Repeat Keyword 2 times CLICK DOWN
CLICK OK
$(Result) VERIFY IMAGE Put Device_To_Sleep
Run Keyword If '$(Result)''Pass' Log to Console Navigated To Put Device To Sleep Screen
ELSE Fail Not Navigated To Put Device To Sleep Screen Repeat Keyword $(time('No_Of_Times_Down' CLICK DOWN Repeat Keyword 2 times CLICK OK
$(Result) VERIFY IMAGE $(time('Reference_Image']]
0.9
Run Keyword If '$(Result)' 'Pass' Log to Console "Put Device To
Sleep Screen" Time Is Changed To $(time['Waiting Time']}
ELSE Fail "Put Device To Sleep Screen" Time Is Not Changed To $(time('Waiting_Time'11
CLICK BACK
TOGGLING POWER SAVING MODE
[Arguments] $ton_off)
CLICK OK
﻿

$(Result) VERIFY IMAGE PowerSavingMode Ston_offi
Run Keyword It Result-Face Log To Console Power Saving Mode Is Toggled
ELSE Fall Power Saving Mode Is Not Toggled
REMOVING GOOGLE ACCOUNT FROM SETTINGS
[Documentation] This Keyword will remove already added google account from Accounts & Sign In Screen
CLICK OK
$/Result) VERIFY IMAGE Accounts Signin
Run Keyword If 'Result)''Pass' Log To Console Accounts & Sign In Screen Is Displayed
ELSE Fail Accounts & Sign In Screen Is Not Displayed CLICK OK
$(Result) VERIFY IMAGE Accounts Opts
Run Keyword If '$Result)'--'Pass' Log To Console Accounts & Sign In Screen Options Are Displayed
... ELSE Fail Accounts & Sign In Screen Options Are Not Displayed Log To Console Verifying "Remove Account"!!!
CLICK DOWN
CLICK OK
$(Result) VERIFY IMAGE RemoveAccount_Screen
Run Keyword If
Screen Is Displayed
'$(Result)''Pass' Log To Console Remove Account
ELSE Fail Remove Account Screen Is Not Displayed
CLICK DOWN
CLICK OK
Sleep 2
$(Result) VERIFY IMAGE AddAccount
Run Keyword If '$Result)''Pass' Log To Console Google Account Is Removed Successfully
ELSE Fail Google Account Is Not Removed
Repeat Keyword 2 times CLICK BACK
REMOVING BUG GENERATED REPORT FROM NOTIFICATION SCREEN
Log To Console Removing Bug Generated Report Notification!!! Sleep im
CLICK RIGHT
$(Result1) VERIFY IMAGE
CrossIcon_Highlight
Run Keyword If 'S Result1) 'Pass CLICK OK
ELSE Fail Cross Icon Is Not Selected To Remove Bug Generated Report Notification
$(Result2) VERIFY IMAGE BugIcon_Notificationscreen
Run Keyword If '$Result2] 'Pass' Fail Bug Generated Report Notification Is Still Displaying
ELSE Log To Console Bug Generated Report Notification Is Removed VERIFY VIDEO PLAY
Sleep 5s
$(Result1) CAPTURE PAGE Screen! Sleep 30s
$(Result2} CAPTURE PAGE Screen2
$/Result) COMPARE SCREEN $Result1)
Run keyword If
'$Result' -'Fail'
Video Is Not Playing
$(Result2)
Log To Console Video Is Playing
.. ELSE Fail
LAUNCH PROGRAM GUIDE FROM GUIDE ROU KEY
CLICK GUIDE
Log To Console Verifying EPG!!!
Sleep
3s
$(Result) VERIFY IMAGE EPG Screen
﻿

[Return] $Result)
DELETE CONTENT
4
[Arguments] $(label)-
$(Result) VERIFY IMAGE Delete_Watchlist
Run keyword If '$Result' -- 'Pass' CLICK OK ELSE Fail Not Focused On Delete Icon Log To Console Selecting Content To Delete CLICK OK
${Result) VERIFY IMAGE SelectedTo_Delete Run keyword If
ELSE Fail
CLICK OK
Run Keyword If
'S/Result)'--'Pass' CLICK UP
Contents Are Not Selected To Delete
'S(label) == 'Recordings' DELETE CONTENT CONFIRMATION
Log To Console Content Is Deleting
$(Result) VERIFY IMAGE Delete Watchlist
[Return]
$(Result)
DELETE CONTENT CONFIRMATION
$(Result) VERIFY IMAGE ON SCREEN Delete Confirmation
Run keyword If ELSE Fail Log To Console
CLEAR SEARCH HISTORY
'S(Result'--'Pass' CLICK OK
Delete Confirmation Popup Is Not Displayed. Deleting Content
$(Result) NAVIGATE TO ANY OPTION ON MENU ${SEARCH_ICON
Run Keyword If 'S(Result)'--'Pass'
No Search History To Clear
AND RETURN FROM KEYWORD
CLICK BACK
CLICK DOWN
$(Result) VERIFY IMAGE ClearHistory
Run Keyword If
Is Highlighted
Run Keywords Log To Console
'S(Result)''Pass' Log To Console
Clear History
ELSE Fail Clear History Is Not Highlighted CLICK OK
$Result) VERIFY IMAGE Search Screen
Run Keyword If
Is Cleared
$(ResultPass' Log To Console
Search History
ELSE Fail Search History Is Not Cleared
Selecting Search Icon On Keyboard
$(Result) VERIFY IMAGE Keypad
Run Keyword If
Displayed
'S/Result='Pass' Log to Console KeyPad Is
ELSE Fail KeyPad Is Not Displayed
Repeat Keyword 3 times CLICK DOWN
CLICK LEFT
$(Result) VERIFY IMAGE SearchIcon_KB_Highlight
Run Keyword If '$Result)''Pass' Log to Console Search Icon Is Highlighted
ELSE Fail Search Icon Is Not Highlighted
CLICK OK
Sleep 2s
$(Result) VERIFY IMAGE Keypad
Run Keyword If '$Result)''Pass' Fail Search Icon Is Not Selected
ELSE Log to Console Search Icon Is Selected
AGE RATING CONTENT
$(Result) LAUNCHING SPECIFIC OPTION FROM SETTINGS SCREEN
﻿

SISETTINGS IN THE TV APPLICATIONE
Run keyword If
Is Launched
(Result)-Pass Log To Console Setting Screen
ELSE Fail Setting Screen Is Not Launched
$(Result)
BES SECURITY
NAVIGATING TO PARTICULAR OPTION IN SELECTED SETTINGS OPTIONS
Run Keyword I 'SIResult) "Pans Log to Console Security Option Is Displayed
ELSE Fall Security Option Is Not Displayed
Sleep 25
Repeat Keyword 2 times CLICK DOWN
$(Result) VERIFY IMAGE Age Rating 0.997 Run Keyword If 'SiResult)''Pass CLICK OK
*** ELSE Fail Already Enabled Age Rating. $(Result) VERIFY IMAGE Age RatingPin
Run Keyword If **10-Pass INPUT TEXT SOLD PIRE ELSE Fall Age Raing Pin Not Enabled.
Sleep 2 $Result) [Return]
VERIFY IMAGE Age RatingEnabled 0,997 StRemul
UNLOCK AGE RATING CONTENT
$(Result)
LAUNCHING SPECIFIC OPTION FROM BETTINGS SCREEN
$1BETTINGS IN THE TV APPLICATIONS
Run keyword If '21esults 'a' Log To Console Setting Screen Ia Launched
ELSE FALL Setting Screen Is Not Launched
$(Result) NAVIGATING TO PARTICULAR OPTION IN SELECTED SETTINGS OPTIONS
Run Keyword It
Is Displayed
"SERIES 'Pass Log to Console Security Option
ELSE Fall Security Option Is Not Displayed
Sleep 2
#Remalt)
Repeat Keyword 2 times CLICK DOWN
VERIFY IMAGE Age RatingEnabled
0.997
Run Keyword If ''Pass CLICK OK
ELSE Fall Age Rating Is Not Enabled
VERIFY IMAGE Age RatingPin
Run Keyword It Result'--'P INPUT TEXT FOLD PINE ELSE Fall Not Entered Pis
Sleep 25
$Resulti VERIFY IMAGE Age Rating 0.997 Bun Xeyword If 'Result-'Pass
Log To Console Unlocked Content
ELSK Fail Age Rating Is Not Unlocked
UNLOCK ADULT CONTENT
UNLOCK AGE RATING CONTENT
CLICK DOWN
3/Result) VERIFY IMAGE
Adult ContentEnabled
CLICK 0.997
0.997 OK
Run keyword 11 $Result)-- "Pass" $(Result) VERIFY IMAGE Adult Content Run keyword If
Content Lock In Reneved.
ELSE Fall Content Is Not Unlocked.
LAUNCH EPG FROM NOW ON TV LIST
CLICK HOME
Log To Console Verifying HOME!!!
$Result) VERIFY IMAGE Menubar Repeat Keyword 2 CLICK DOWN
Log To Console Verifying MowOn Home!!!
﻿

$[Result) VERIFY IMAGE NowOn Home CLICK LEFT
CLICK
OR
Log To Console Verifying EPG!!! $Result) VERIFY IMAGE EPG Screen [Return) $(Result)
Selecting Content To Play
FOR $11) IN RANGE 20
CLICK OF
Sleep 25
3(Result) VERIFY IMAGE Play Zoom
Run Feyword If "$(Baralt
"Pass" Run Heywords Log To Console
Watch Option Is Available For The Selected Content
END
AND CLICK OR
AND Exit For Soop
ELSE Bun Keywords CLICK BACK
AND CLICK RIGHT
Run Reyword It - Fail Fail Not Able to Select Content With Watch Option
NAVIGATE TO MY CHANNELS
S:Result) LAUNCHING SPECIFIC OPTION FROM SETTINGS SCREEN STR Run keyword if SIResultPass Log To Console MyTV Screen Is Launched
ELSE Fall MyTV Screen Is Not Launched
Repeat Reyword 2 times CLICK DOWN
3/Result) VERIFY IMAGE My Channels
Run keyword It SesultPass CLICK LEFT CLICK OK
$(Result) VERIFY IMAGE All Channelsty
[Return]
ADD CHANNEL FAVOURITES
S:Result) NAVIGATE TO MY CHANNELS
Run keyword If
Sleep 28
CLICK RIGHT
CLICK OK
FOR $14)
IN RANGE
4
CLICK
DOWN
CLICK OK
END
$Result)
NAVIGATE TO FAVOURITES IN HOME SCREEN [Return] StResult
REMOVE FAVOURITES
$Result) NAVIGATE TO MY CHANNELS
Bu keyword It Pesult)''Pass' CLICK RIGHT CLICK OK
FOR $11) IN RANGE 4
END
CLICK DOWN
CLICK OK
$(Result)
NAVIGATE TO FAVOURITES IN HOME SCREEN [Return] 5(Result)
REMOVE ALL FAVOURITES USING RESET
S:Result) NAVIGATE TO MY CHANNELS
Run keyword If "Result "Pass" Repeat keyword 3 times CLICK
﻿

RIGHT
CLICK OK
$(Result) VERIFY IMAGE
Reset Favourite
Run keyword If 'S(Result)--Pass CLICK OK
CLICK OK
$(Result)
[Return]
VERIFY IMAGE
$Result)
NAVIGATE TO HOME WATCH NEXT
Cleared Favourites
GO TO HOME PAGE
Repeat Keyword 3 times
CLICK DOWN
Favourite Home
$(Result) VERIFY IMAGE
Run keyword If $(Result)'--'Pass' CLICK DOWN $(Result) VERIFY IMAGE WATCH NEXT
[Return] $(Result)
NAVIGATE TO HOME WATCHLIST
DOWN
GO TO HOME PAGE
Repeat Keyword 3 times CLICK DOWN
$[Result) VERIFY IMAGE
Favourite Home
Run keyword If 'S/Result)''Pass' Repeat Keyword 2 times
ELSE CLICK DOWN
$Result) VERIFY IMAGE Watchlist Home
[Return] $(Result)
LAUNCH SEARCH SCREEN
$Result) NAVIGATE TO ANY OPTION ON MENU SEARCH_ICON
CLICK
Run Keyword If 'SIResult)''Pass Run Keywords Log To Console Search Screen Is Displayed
AND RETURN FROM KEYWORD
CLICK BACK
CLICK DOWN
$(Result) VERIFY IMAGE ClearHistory
Run Keyword If '5(Result)''Pass' CLICK OK ELSE Fall Clear History Is Not Highlighted
$(Result) VERIFY IMAGE Search Screen
Run Keyword If
Is Displayed
'S(Result)''Pass' Log To Console Search Screen
ELSE Fail Search Screen Is Not Displayed
ENABLE PARENTAL LOCK FOR 7PLUS
$(Result) LAUNCHING SPECIFIC OPTION FROM SETTINGS SCREEN $(SETTINGS IN THE TV APPLICATION)
Run keyword If
Is Launched
'S/Result)''Pass' Log To Console Setting Screen
ELSE Fail Setting Screen Is Not Launched
$(Result) NAVIGATING TO PARTICULAR OPTION IN SELECTED SETTINGS OPTIONS SIS PARENTAL)
Run Keyword If
Is Displayed
ELSE Fail
Repeat Keyword
CLICK OK
'S(Result) 'Pass' Log to Console Security Option
Security Option Is Not Displayed 3 times CLICK DOWN
$(Result) VERIFY IMAGE Age Rating Pin Run Keyword If '$(Result)''Pass' sleep 2s
$(Result) VERIFY IMAGE
INPUT TEXT STOLD PINI
Parental 7plus
0.99
Run Keyword If '$Result)''Pass Log To Console
Enabled
﻿

Parental Rating For Age 7 Plus
NAVIGATING TO APPS
${Result) NAVIGATE TO ANY OPTION ON MENU $(APPLICATIONS) Run keyword If '$ (Result)''Pass' Log To Console Applications
Screen Is Displayed
ELSE Fail Applications Screen Is Not Displayed
CLICK DOWN
${Result) VERIFY IMAGE Google PlayStore
Run keyword If '${Result) == 'Pass' CLICK OK
Log To Console Verifing whether logged into gmail
$ (Result) VERIFY IMAGE Google Play Signin
Run keyword If '${Result) == 'Pass' SIGN IN TO GOOGLE ACCOUNT ELSE Log To Console Already Signed In
${Result) VERIFY IMAGE Google Play
Run keyword If '$ (Result)' == 'Pass' CLICK UP ELSE Fail Not Navigated To Play Store Page ${Result) VERIFY IMAGE Google PlayApps [Return]
INSTALL APP
${Result)
${Result) NAVIGATING TO APPS
Run keyword If '$ (Result)' -- 'Pass' CLICK LEFT ${Result) VERIFY IMAGE App_SearchScreen
Run keyword If
launched
'$(Result)'
'Pass' Log To Console
Search Screen
ELSE Fail Search Home Screen Is Not Displayed CLICK DOWN
CLICK LEFT
${Result) VERIFY IMAGE Run keyword If
times CLICK RIGHT
Gboard Image
'${Result)' == 'Pass' Run Keywords Repeat keyword
AND CLICK DOWN
${Result) VERIFY IMAGE Hotstar search
'${Result)'
== 'Pass'
Repeat keyword 2 times CLICK OK
Repeat keyword 2 times CLI
Run keyword If
UP
${Result)
VERIFY IMAGE install
Run keyword If
'${Result)'
'Pass'
CLICK
OK




