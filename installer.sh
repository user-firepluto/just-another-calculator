#!/bin/bash
chmod +x calc
chmod +x calc.py
chmod +x remove.sh
mkdir /home/$USER/.miniprojects/calc
sudo cp calc.py /home/$USER/.miniprojects/calc
sudo cp remove.sh /home/$USER/.miniprojects/calc
sudo cp calc /usr/local/bin
echo "Instalation completed"

