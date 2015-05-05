from controlhost import Client

client = Client('localhost')
client._connect()
client.subscribe('foo')
print client.get_message()
client._disconnect()
