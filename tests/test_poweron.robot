*** Settings ***
Library          ../lib/rest_client.py
Resource         ../lib/resource.txt
Resource         ../lib/connection_client.robot
Resource         ../lib/utils.robot

Suite setup          Login and Verify Connection
Suite Teardown       Close All Connections

*** Variables ***
${Retry}         5 min
${Interval}      30s

*** Test Cases ***
Test PowerOff System
     [Documentation]   poweroff using POST method\n
     ${resp} =   Post Request   ${BASE_URI}   /Chassis/1/Actions/Reset   ForceOff
     Should be equal as strings   ${resp}   ${HTTP_OK}

     ${state}=   Get System State
     Log To Console    \n IPL Current System State: ${state}

     Log To Console    \n Wait for system to poweroff state
     Wait Until Keyword Succeeds    ${Retry}    ${Interval}
     ...    Verify System State   standby
     Log To Console    \n System Powered Off successfully

Test PowerOn System
     [Documentation]   PowerOn using POST method\n
     ${resp} =   Post Request   ${BASE_URI}   /Chassis/1/Actions/Reset   powerOn
     Should be equal as strings   ${resp}   ${HTTP_OK}

     ${state}=   Get System State
     Log To Console    \n IPL Current System State: ${state}

     Log To Console    \n Wait for system to runtime state
     Wait Until Keyword Succeeds    ${Retry}    ${Interval}
     ...    Verify System State   runtime
     Log To Console    \n System Powered On successfully


*** Keywords ***

