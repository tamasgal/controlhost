from controlhost import Client

client = Client('localhost')
client._connect()
client.subscribe('foo')

try:
    while True:
        prefix, message = client.get_message()
        print prefix.tag
        print prefix.length
        print message
except KeyboardInterrupt:
    client._disconnect()
