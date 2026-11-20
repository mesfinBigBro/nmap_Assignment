#!/bin/bash

echo $2 $1
nmap --script $2 $1

#E.g. == 4_nmap_with_NES.sh 127.0.0.1 vuln

