#!/bin/bash
#update.sh - update simple-ducky and all submodules
# From https://github.com/skysploit/simple-ducky/blob/master/update.sh

#update simple-ducky
cd /usr/share/simple-ducky
git pull

# Update submodules
git submodule foreach git checkout master
git submodule foreach git pull
git commit -a -m 'updated submodules'
