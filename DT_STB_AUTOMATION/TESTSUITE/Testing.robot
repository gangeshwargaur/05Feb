#Testing.robot
//** under testsuit folder**
***
Settings
***
Resource
${EXECDIR}/TestScripts/LIB/ROBOT/STB_Functions.robot
Library $(EXECDIR)/TestScripts/LIB/PYTHON/STB.py $(EXECDIR} Variables
$(EXECDIR)/TestScripts/VARIABLES/Config.py
Library $(EXECDIR)/TestScripts/LIB/PYTHON/Status TC.py
Library
${EXECDIR)/TestScripts/LIB/PYTHON/TeardownStatusTC.py
*** Test Cases ***
Capturing Image
[Tags] Tagl
${Result) CAPTURE REFERENCE IMAGE google_play_movies_&_TV Log To Console ${Result}
Test2: Verifings
