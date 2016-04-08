#!/bin/bash

wget -qO - https://deb.packager.io/key | sudo apt-key add -
echo "deb https://deb.packager.io/gh/pkgr/gogs trusty pkgr" | sudo tee /etc/apt/sources.list.d/gogs.list
sudo apt-get update
sudo apt-get install gogs --fix-missing

