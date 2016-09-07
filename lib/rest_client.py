#!/usr/bin/python
'''
#############################################################
#    @file     rest_client.py
#    @author:  George Keishing
#
#    @brief    Request methods for Red Fish Automation using
#              robot framework
#############################################################
'''
import requests
import os
import json
from robot.libraries.BuiltIn import BuiltIn

class rest_client():

    ########################################################################
    #   @brief    Request GET method
    #   @param    base_url: @type string: URL to base redfish
    #   @param    i_url: @type string: Suffix string of the path
    #   @return   HTTP REST json response data
    ########################################################################
    def get_request(self, base_url, i_url=""):
        i_url = base_url + i_url
        self.write_to_console(i_url)
        r = requests.get(i_url, verify=False)
        response = r.json()
        self.json_pretty_format(response)
        return  response

    ########################################################################
    #   @brief    Request PATCH method
    #   @param    base_url: @type string: URL to base redfish
    #   @param    i_url: @type string: Suffix string of the path
    #   @param    parm: @type string: data to be written
    #   @return   HTTP REST status code
    ########################################################################
    def patch_request(self , base_url, i_url, parm):
        i_url = base_url + i_url
        self.write_to_console(i_url)
        pdata = json.dumps({'Name' : parm})
        self.json_pretty_format(pdata)
        r = requests.patch(i_url, data = pdata)
        self.write_to_console (r.status_code)
        return  r.status_code

    ########################################################################
    #   @brief    Print the JSON data pretty format to Console
    #   @param    i_response: @type json: JSON response data
    #   @return   None
    ########################################################################
    def json_pretty_format(self, i_response):
        self.write_to_console(json.dumps(i_response, indent=4))

    ########################################################################
    #   @brief    robot console logging
    #   @param    i_str: @type string: string name
    #   @return   None
    ########################################################################
    def write_to_console(self, i_str):
        BuiltIn().log_to_console(i_str)

    ########################################################################
    #   @brief    Returns the stripped system name
    #   @param    i_str: @type string: string name
    #   @return   system name
    ########################################################################
    def get_system_string(self, i_str):
        return i_str.rsplit('/', 1)[-1]
