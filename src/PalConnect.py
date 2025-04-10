import json
import base64
import requests

class PalConnect:
    _host = None
    _auth = None

    def __init__(self, username, password, ip="localhost", port=8212):
        self._make_connection(username, password, ip, port)

    def server_info(self):
        try:
            response = requests.request("GET", self._make_url("info"), headers=self._make_header(), data={})
            server_info_dict = [json.loads(response.text)]

        except requests.exceptions.ConnectionError as e:
            print(f"Error connecting to server '{self._make_url()}'")
            server_info_dict = None

        return server_info_dict
        
    def get_players(self):
        try:
            response = requests.request("GET", self._make_url("players"), headers=self._make_header(), data={})
            player_list = [json.loads(response.text)][0].get("players")

        except requests.exceptions.ConnectionError as e:
            print(f"Error connecting to server '{self._make_url()}'")
            player_list = None

        return player_list
    
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
    
    def _make_connection(self, username, password, ip, port):
        self._host = f"{ip}:{port}"

        self._auth = f"Basic {(base64.b64encode(bytes(f'{username}:{password}', 'utf-8'))).decode('utf-8')}"

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