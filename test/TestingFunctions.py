import os
import sys
import json

global SRC_DIR; SRC_DIR = os.path.dirname(os.path.abspath(__file__))
global PROGRAM_DIR; PROGRAM_DIR = os.path.dirname(SRC_DIR)
sys.path.append(PROGRAM_DIR)

from src.PalFuncs import PalFuncs

class Testing:
    api_connection = None

    def __init__(self, file_name="login_file"):
        print("Getting username and password")
        username, password = self._get_usr_and_pass(file_name)

        print("Making connection values to rest API")
        self.api_connection = PalFuncs(username, password)

    def _get_usr_and_pass(self, file_name):
        print("Checking for login credential file")
        '''
        Expected json format:
        {
            "username":<username>,
            "password":<password>
        }
        '''
        #Checks if the credentials file can be found first
        if os.path.exists(f"{file_name}.json"):
            #Opens the file and gets the json data out and makes it into a dict
            with open(f"{file_name}.json", "r") as file:
                data = json.load(file)
        else:
            print(f"{file_name}.json not found. Place file in same directory as the program file(s)")
            sys.exit(-1)

        #Gets the username and password from the dict loaded in
        username = data.get("username")
        password = data.get("password")

        if username == None or password == None:
            print("Username or password not found")
            sys.exit(-1)

        return(username, password)

    def get_players(self):
        if self.api_connection:
            players = self.api_connection.get_players()
            print("Players:")
            if players:
                for key, value in players.items():
                    print(f"{key}: {value}")
            else:
                print("No player data found")
        else:
            print("No api connection made")
        print()

    def get_server_info(self):
        if self.api_connection:
            server_info = self.api_connection.server_info()
            print("Server info: ")
            if server_info:
                for key, value in server_info.items():
                    print(f"{key}: {value}")
            else:
                print("No server data found")
        else:
            print("No api connection made")
        print()

    def get_server_settings(self):
        if self.api_connection:
            server_settings = self.api_connection.get_server_settings()
            print("Server settings: ")
            if server_settings:
                for key, value in server_settings.items():
                    print(f"{key}: {value}")
            else:
                print("No server settings found")
        else:
            print("No api connection made")
        print()

    def get_server_metrics(self):
        if self.api_connection:
            server_metrics = self.api_connection.get_server_metrics()
            print("Server metrics: ")
            if server_metrics:
                for key, value in server_metrics.items():
                    print(f"{key}: {value}")
            else:
                print("No server metrics found")
        else:
            print("No api connection made")
        print()

    def send_message(self):
        if self.api_connection:
            message = "Hello y'all"
            result = self.api_connection.send_server_message(message)
            print(f"Sending message '{message}': ")
            if result:
                print(f"Return code: {result}")
            else:
                print("Error while sending message")
        else:
            print("No api connection made")
        print()

    def shutdown_server(self):
        if self.api_connection:
            result = self.api_connection.shutdown_server()
            print(f"Shutting down server: ")
            if result:
                print(f"Return code: {result}")
            else:
                print("Error while shutting down server")
        else:
            print("No api connection made")
        print()