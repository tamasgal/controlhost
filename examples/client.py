from controlhost import Client

with Client('131.188.161.241') as client:
    client.subscribe('foo')
    try:
        while True:
            prefix, message = client.get_message()
            print prefix.tag
            print prefix.length
            print message
    except KeyboardInterrupt:
        client._disconnect()
