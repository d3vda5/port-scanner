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

print("-"*50)
print("Scanning Target: " + target)
print("scanning started at: " + str(datetime.now()))
a= int(datetime.now())
print("-"*50)
try:
    for port in range(0, 1023):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("Quitting Program!!!!!!")
    sys.exit()
except socket.gaierror: 
    print("\n Hostname Could Not Be Resolved !!!!") 
    sys.exit() 
except socket.error: 
    print("\n Server not responding !!!!") 
    sys.exit()

print("-"*50)
b=int(datetime.now)
print("scanning ended at: " + str(datetime.now()))
print(f"Total Scanning time: {b-a}")