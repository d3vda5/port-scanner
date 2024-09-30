import pyfiglet
import sys
import socket
from datetime import datetime

banner = pyfiglet.figlet_format("PORT SCANNER")
print (banner)

if len(sys.argv)==2:
    target= socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of argument, you have to enter the IP")

port = int(input("\n Enter the port number you want to scan: "))
print("Scanning Target: " + target)
print("scanning started at: " + str(datetime.now()))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)
result = s.connect_ex((target,port))
if result == 0:
    print(f"Port {port} is open")
s.close

print("scanning ended at: " + str(datetime.now()))