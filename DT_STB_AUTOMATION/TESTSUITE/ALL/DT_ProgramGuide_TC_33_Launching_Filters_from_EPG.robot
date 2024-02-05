*** Settings ***
Resource  $(EXECDIR)/TestScripts/LIB/ROBOT/STB_Functions.robot
Library   $(EXECDIR)/TestScripts/LIB/PYTHON/STB.py $EXECDIR)
Variables  $(EXECDIR)/TestScripts/VARIABLES/Config.py
Library    $(EXECDIR)/TestScripts/LIB/PYTHON/StatusTC.py
Library     $4EXECDIR)/TestScripts/LIB/PYTHON/TeardownStatusTC.py
 
*** Test Cases ***
DT_ProgramGuide TC 33: Verify user is able to launch filters in program guide using Filter icon
 [Setup] TEST SETUP
 CLICK GUIDE
 sleep 55
 $Result) VERIFY IMAGE EPG Screen
 Run keyword If
 Displayed
 CLICK
 Run Keyword If  '${Result}' -- 'Pass' Log To Console Guide Screen Is  Displayed
 ... ELSE Fail Guide Screen Is Not Displayed
 CLICK NUM1

 Sleep 35
 Repeat Keyword 2 times CLICK UP
 ${Result) VERIFY IMAGE EPG Filter
 Run keyword If $Result)''Pass' CLICK OK
 $(Result) VERIFY IMAGE Filter options
 Run keyword If 'S(Result)=='Pass' Log To Console EPG Filter
 Options Is Displayed
 ... ELSE Fail EPG Filter Options Not Displayed
 [Teardown] Run Keywords
 Run Keyword If Test Passed TEST TEARDOWN DT_ProgramGuide TC_33_Launching Filters_from_EPG AND Run Keyword If Test Failed TEST TEARDOWN
   DT ProgramGuide TC_33_Launching_Filters_from_EPG
