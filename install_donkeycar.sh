#!/bin/bash

set -uex

sudo dnf install pip -y
pip install -r requirements.txt
pip install git+https://github.com/tawnkramer/gym-donkeycar
wget https://github.com/tawnkramer/gym-donkeycar/releases/download/v21.12.11/DonkeySimLinux.zip && unzip DonkeySimLinux.zip
chmod u+x DonkeySimLinux/donkey_sim.x86_64
echo "IP:", ifconfig | grep inet
DonkeySimLinux/donkey_sim.x86_64


