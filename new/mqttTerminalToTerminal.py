sudo apt-get install -y mosquitto mosquitto-clients

in first terminal
mosquitto_sub -h localhost -v -t test_channel

in new terminal
mosquitto_pub -h localhost -t test_channel -m "Hello Raspberry Pi"