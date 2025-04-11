from TestingFunctions import Testing

if __name__ == "__main__":
    print("Starting program")

    print("Making connection values to rest API")
    test_funcs = Testing()
    
    print("Getting players")
    test_funcs.get_players()

    #print("Getting server info")
    #test_funcs.get_server_info()

    #print("Getting server settings")
    #test_funcs.get_server_settings()

    #print("Getting server metrics")
    #test_funcs.get_server_metrics()

    #print("Sending message to server")
    #test_funcs.send_message()

    #print("Sending shutdown to server")
    #test_funcs.shutdown_server()