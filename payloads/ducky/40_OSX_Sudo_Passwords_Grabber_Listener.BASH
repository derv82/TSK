#!/bin/bash
while [ true ]
do
netcat -vv -lp 1337 >> passwd.txt
done
