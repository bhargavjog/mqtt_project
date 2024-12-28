import asyncio
import gmqtt

STOP = asyncio.Event()

def on_connect(client, flags, rc, properties):
    print("Connected")
    client.subscribe('/events')

def on_message(client, topic, payload, qos, properties):
    print(f"Received message '{payload.decode()}' on topic '{topic}'")

def on_disconnect(client, packet):
    print("Disconnected")

def on_subscribe(client, mid, qos, properties):
    print("Subscribed")

async def main():
    client = gmqtt.Client("mqtt-listener")

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe

    await client.connect('localhost', 1883)
    await STOP.wait()

if __name__ == "__main__":
    asyncio.run(main())
