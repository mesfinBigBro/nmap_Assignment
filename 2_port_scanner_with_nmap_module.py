import nmap
import sys
target = sys.argv[1]
port = sys.argv[2]
Scanner=nmap.PortScanner()
result=Scanner.scan(str(target),port)
result=result['scan'][target]['tcp'][int(port)]['state']
print(f'port-{port} is {result}')
