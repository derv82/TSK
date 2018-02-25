#!/bin/bash
# install.sh - install simple-ducky
# From https://github.com/skysploit/simple-ducky/blob/master/install.sh


if [ "${UID}" != "0" ]; then
	echo -e "\e[1;31m[!] This script must be run as root\e[0m" 1>&2
	exit 1
else
	if ! [ -a /usr/share/simple-ducky/simple-ducky.sh ] && ! [ -a /usr/share/simple-ducky/update.sh ]; then
		git clone --recursive https://github.com/gitbrew/simple-ducky.git /usr/share/simple-ducky
	fi
	ln -sf /usr/share/simple-ducky/misc/dbd-conf/* /usr/share/simple-ducky/misc/dbd/conf/
	ln -sf /usr/share/simple-ducky/simple-ducky.sh /usr/bin/simple-ducky
	ln -sf /usr/share/simple-ducky/update.sh /usr/bin/simple-ducky-update
fi
