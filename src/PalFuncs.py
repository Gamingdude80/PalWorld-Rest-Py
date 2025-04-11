import json
import requests

from src.PalConnect import PalConnect

class PalFuncs:
    api_connection = None

    def __init__(self, username, password):
        self.api_connection = PalConnect(username, password)

    def _server_request(self, type, destination, payload={}):
        try:
            response = requests.request(type.upper(),
                                        url=self.api_connection._make_url(destination),
                                        headers=self.api_connection._make_header(),
                                        data=payload)
            if response:
                #If there was a response but no text inside, sends back the response
                if response.text:
                    output = json.loads(response.text)
                else:
                    output = response.status_code
            else:
                output = None

        except requests.exceptions.ConnectionError as e:
            print(f"Error connecting to '{self.api_connection._make_url(destination)}', Request type: {type}")
            output = None

        return output
           
    def server_info(self):
        return self._server_request("GET", "info")
        
    def get_players(self):
        output = self._server_request("GET", "players")
        return output.get("players") if output != None else None
    
    def get_server_settings(self):
        return self._server_request("GET", "settings")
    
    def get_server_metrics(self):
        return self._server_request("GET", "metrics")
    
    def send_server_message(self, message):
        payload = json.dumps({
            "message": message
            })
        return self._server_request("POST", "announce", payload)
    
    #TODO test this function
    def kick_player(self, userid, message):
        #Steam user id here. steam_00000000000000000
        payload = json.dumps({
            "userid": userid,
            "message": message
            })
        return self._server_request("POST", "kick", payload)

    #TODO test this function
    def ban_player(self, userid, message):
        #Steam user id here. steam_00000000000000000
        payload = json.dumps({
            "userid": userid,
            "message": message
            })
        return self._server_request("POST", "ban", payload)
    
    #TODO test this function
    def unban_player(self, userid):
        #Steam user id here. steam_00000000000000000
        payload = json.dumps({
            "userid": userid,
            })
        return self._server_request("POST", "unban", payload)
    
    #TODO test this function
    def save_world(self):
        return self._server_request("POST", "save")
    
    def shutdown_server(self, waittime=30, message=None):
        if message == None:
            message = f"Shutdown in {waittime} seconds"

        payload = json.dumps({
            "waittime": waittime,
            "message": message
            })
        return self._server_request("POST", "shutdown", payload)
    
    #TODO test this function
    def force_stop_server(self):
        return self._server_request("POST", "stop")