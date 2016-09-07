import requests
import os
import json
from robot.libraries.BuiltIn import BuiltIn

class rest_client():

    def get_request(self, base_url, i_url=""):
        i_url = base_url + i_url
        self.write_to_console(i_url)
        r = requests.get(i_url, verify=False)
        response = r.json()
        self.json_pretty_format(response)
        return  response

    def patch_request(self , base_url, i_url, parm):
        i_url = base_url + i_url
        self.write_to_console(i_url)
        #headers = {'content-Type' :'application/json'}
        #pdata = json.dumps({'data' : parm})
        pdata = json.dumps({'Name' : parm})
        self.json_pretty_format(pdata)
        r = requests.patch(i_url, data = pdata)
        self.write_to_console (r.status_code)
        return  r.status_code

    def json_pretty_format(self, i_response):
        #print(json.dumps(response, indent=2))
        self.write_to_console(json.dumps(i_response, indent=4))

    def write_to_console(self, s):
        BuiltIn().log_to_console(s)

    ########################################################################
    #   @brief    Returns the stripped system name
    #   @param    i_str: @type string: string name
    #   @return   system name
    ########################################################################
    def get_system_string(self, i_str):
        return i_str.rsplit('/', 1)[-1]
