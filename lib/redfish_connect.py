import   redfish
import   json

class redfish_connect(object):

    def __init__(self, host_ip):
        r"""
        initialize redfish client connection to host.
        """

        self.base_url = "https://" + host_ip
        self.username = "root"
        self.password = "myPassword"
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


    def json_data(self, response):
        r"""
        Return JSON converted data.
        """
        json_data = json.loads(response.text)
        return json_data


    def json_pretty_print(self, json_data):
        r"""
        JSON data pretty print the formatted output on console.
        """
        print json.dumps(json_data, sort_keys=True, indent=4)


# Example how to use:
connection = redfish_connect("XX.XX.XX.XX")
response = connection.get_method("Systems")
json_data = connection.json_data(response)
connection.json_pretty_print(json_data)
connection.logout_session()
