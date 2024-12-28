import asyncio     # Import asyncio for asynchronous programming
import gmqtt       # Import gmqtt for MQTT client functionality

# Create an event that will stop the main event loop when triggered
STOP = asyncio.Event()

# ------------------------------
# CALLBACK FUNCTIONS
# ------------------------------

# This function is called when the client successfully connects to the MQTT broker
def on_connect(client, flags, rc, properties):
    print("Connected")             # Print a message to confirm the connection
    client.subscribe('/events')    # Subscribe to the topic '/events' to listen for messages


# This function is triggered when a message is received on the subscribed topic
def on_message(client, topic, payload, qos, properties):
    print(f"Received message '{payload.decode()}' on topic '{topic}'")             # Prints the received message and the topic it was received on

# This function is triggered when the client disconnects from the MQTT Broker
def on_disconnect(client, packet):
    print("Disconnected")

# This function is called when the client disconnects from the MQTT broker
def on_subscribe(client, mid, qos, properties):
    print("Subscribed")


# ------------------------------
# ASYNCHRONOUS MAIN FUNCTION
# ------------------------------

# Define the main asynchronous function that sets up and runs the MQTT client
async def main():
    # Create an MQTT client instance with a client ID 'mqtt-listener'
    client = gmqtt.Client("mqtt-listener")

    # Attach callback functions to handle various client events
    client.on_connect = on_connect        # Trigger on successful connection
    client.on_message = on_message        # Trigger when a message is received
    client.on_disconnect = on_disconnect  # Trigger when disconnected
    client.on_subscribe = on_subscribe    # Trigger when subscribed to a topic

    # Attempt to connect to the MQTT broker running on localhost at port 1883
    await client.connect('localhost', 1883)
    
    # The program will wait indefinitely until the STOP event is triggered
    await STOP.wait()

# ------------------------------
# RUN THE PROGRAM
# ------------------------------
if __name__ == "__main__":
    asyncio.run(main())
