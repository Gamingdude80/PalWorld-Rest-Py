import base64

class PalConnect:
    _host = None
    _auth = None

    def __init__(self, username, password, ip="localhost", port=8212):
        self._host = f"{ip}:{port}"
        self._auth = f"Basic {(base64.b64encode(bytes(f'{username}:{password}', 'utf-8'))).decode('utf-8')}"
    
    def _make_url(self, url_destination):
        if self.get_host():
            url = f"http://{self.get_host()}/v1/api/{url_destination.lower()}"
            return url
        else:
            print(f"Could not get host, host not set")
            return None
    
    def _make_header(self):
        if self.get_auth():
            headers = {
                "Accept": "application/json",
                "Authorization": self.get_auth()
                }
            return headers
        else:
            print(f"Could not get auth token, token not set")
            return None

    def get_host(self):
        if self._host:
            return self._host
        else:
            return None
        
    def get_auth(self):
        if self._auth:
            return self._auth
        else:
            return None