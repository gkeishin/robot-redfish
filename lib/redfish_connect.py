import   redfish

r"""
To use this code:
    pip install redfish
"""

class redfish_connect(object):

    def __init__(self, host_ip):
        r"""
        initialize redfish client connection to host.
        """

        self.base_url = "https://" + host_ip
        self.username = "root"
        self.password = "mysecretePassword"
        self.default_prefix="/redfish/v1"

        self.robj = redfish.redfish_client(base_url=self.base_url,
                                           username=self.username,
                                           password=self.password,
                                           default_prefix=self.default_prefix)

        self.robj.login(auth="session")

        self.session_key = self.robj.get_session_key()
    

    def get_method(self, resource_path):
        r"""
        Get the resource and return response msg.
        """
        uri_path = '/redfish/v1/' + resource_path
        response = self.robj.get(uri_path)

        print ("HTTPS response : %s" % str(response.status))

        return response


    def logout_session(self):
        r"""
        Logout redfish session.
        """
        self.robj.logout()



# Example:
connection = redfish_connect("XX.XX.XX.XX")
response = connection.get_method("Systems")
print ("%s\n" % response)
connection.logout_session()
