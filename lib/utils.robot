*** Settings ***
Resource        resource.txt


*** Keywords ***

Get System State
   ${state}     Execute Command    ${CMD_IPL_STATE}
   [return]     ${state}

Verify System State
   [Arguments]   ${expect_state}=""
   ${curr_state}=   Get System State
   Should Contain   ${curr_state}   ${expect_state}
