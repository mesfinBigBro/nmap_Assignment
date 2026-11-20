#!/bin/bash

echo $2 $1
nmap --script $2 $1
