import sys,os
IP= sys.argv[1]
port=sys.argv[2]
os.system(f'nmap -p {port} {IP}') 

#E.g. 1_port_scanner_no_nmap_module.py 127.0.0.1 21
