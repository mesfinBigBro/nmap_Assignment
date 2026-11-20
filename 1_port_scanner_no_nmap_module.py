import sys,os
IP= sys.argv[1]
port=sys.argv[2]
os.system(f'nmap -p {port} {IP}') 