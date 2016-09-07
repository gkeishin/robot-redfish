*** Settings ***
Library      ../lib/rest_client.py
Resource     ../lib/resource.txt

*** Variables ***

*** Test Cases ***
Test Base URI
     [Documentation]   Get the Base URI for redfish\n
     Get Request   ${BASE_URI}   

Test Get Manager
     [Documentation]   Get the Managers\n
     Get Request   ${BASE_URI}   /Managers
    
Test Get Chassis
     [Documentation]   Get the Chassis\n
     Get Request   ${BASE_URI}   /Chassis
    
Test Get Systems
     [Documentation]   Get the Systems\n
     Get Request   ${BASE_URI}   /Systems
    
Test Set Systems Name
     [Documentation]   Set System name using Patch method\n
     ${name}=  Get Systems Name
     Get Request   ${BASE_URI}   ${/}Systems/${name}${/}Name
     ${resp} =   Patch Request   ${BASE_URI}   ${/}Systems/${name}${/}Name   Testing-Server
     Should be equal as strings   ${resp}   ${HTTP_OK}
     Get Request   ${BASE_URI}   ${/}Systems/${name}${/}Name

Test Revert Systems Name
     [Documentation]   Revert to original System name using Patch method\n
     ${name}=  Get Systems Name
     Get Request   ${BASE_URI}   ${/}Systems/${name}${/}Name
     ${resp} =   Patch Request   ${BASE_URI}   ${/}Systems/${name}${/}Name   ${name}
     Should be equal as strings   ${resp}   ${HTTP_OK}
     Get Request   ${BASE_URI}   ${/}Systems/${name}${/}Name

*** Keywords ***

Get Systems Name
     ${system_name}=   Get Request   ${BASE_URI}   /Systems
     ${sys_str}=   Get_system string    ${system_name["Members"][0]['@odata.id']}
     [return]  ${sys_str}
