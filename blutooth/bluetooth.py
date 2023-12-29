import bluetooth

# Discover devices
nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))

for addr, name in nearby_devices:
    print("  {} - {}".format(addr, name))

# Specify the address of your device
target_address = "XX:XX:XX:XX:XX:XX"  # Replace with your Bluetooth device's address

# Create a Bluetooth socket
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((target_address, port))

# Send data
sock.send("Hello, Bluetooth!")

# Close the socket
sock.close()
