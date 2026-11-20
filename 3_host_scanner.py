import sys,os
import re
#regex to check whether our ip address is valid or not
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
IP = sys.argv[1]
net_class=sys.argv[2]
def nmap_host(IP):
        #check the ip address is valid or not
        if(re.search(regex, IP)):
                if net_class == 'a':
                        os.system(f'nmap -sn {IP}/8')
                elif net_class == 'b':
                        os.system(f'nmap -sn {IP}/16 -p 22')
                elif net_class == 'c':
                        os.system(f'nmap -sn {IP}/24 -p 22')
                else:
                        print('invalid class')
        else:
                print('invlaid ip address')
nmap_host(IP)                                                                                                                                                 

#how to use it
#3_host_scanner.py 127.0.0.1 c
