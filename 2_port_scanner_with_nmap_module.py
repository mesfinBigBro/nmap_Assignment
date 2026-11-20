import nmap
import sys
target = sys.argv[1]
port = sys.argv[2]
Scanner=nmap.PortScanner()
result=Scanner.scan(str(target),port)
result=result['scan'][target]['tcp'][int(port)]['state']
print(f'port-{port} is {result}')

# E.g.  2_port_scanner_with_nmap.py 127.0.0.1  22
