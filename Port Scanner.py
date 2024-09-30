import pyfiglet
import sys
import socket

banner = pyfiglet.figlet_format("PORT SCANNER")
print (banner)

target= socket.gethostbyname(sys.argv[1])