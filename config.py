# This file affects command injection tests

# Enter the IP address where you have a sniffer or can review logs of
# incoming connections
IP_ADDRESS = '' # If empty, will default to 127.0.0.1

# Enter the port you would like to attempt to send TCP requests
# to via WGET and /dev/tcp
PORT = '' # If empty, will default to 80

# Enter the domain name where you can access logs to see if 
# anyone tries to resolve <randomstring>.example.com
DOMAIN_NAME = '' # If empty, will default to laconicwolf.com
