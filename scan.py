import socket
import re
import sys

def header(lenght):
    print(f"┌{'─'*(lenght-6)}┐")
    print("│","  \033[7m PORT SCANNER \033[0;0;0m  ".center(lenght+4), "│")
    print("│ ", "mateusf.com".center(lenght-10), " │")
    print(f"└{'─'*(lenght-6)}┘")

PORTS = [
    80,
    9595,
    9596,
    8080,
    8888,
    8181,
    9597
]

PORTS = [
    15000,
    3305,
    3306
]

header(26)

ip = ''

if len(sys.argv) > 1:
    ip = sys.argv[1]
else:
    ip = input("IP: ")

print("\nIniciando testes...")
for port in PORTS:            
    ip = re.sub(r"^https?:\/\/", "", ip)
    ip = re.sub(r"\/", "", ip)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)

    if s.connect_ex((ip,port)):
        print("\033[1;30;41m OFF \033[0;0;0m", port)
    else:
        print("\033[1;30;42m ON  \033[0;0;0m", port)

    s.settimeout(None)
