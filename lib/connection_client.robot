*** Settings ***
Library        Telnet
Library        String


*** Keywords ***

Login and Verify Connection
   Open Connection  ${HOST_SYSTEM}    prompt=$
   Login   ${USERNAME}  ${PASSWORD}

