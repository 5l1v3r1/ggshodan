#!/bin/bash


echo -e ">> install chromium-deps"
sudo apt install chromium-browser chromium-chromedriver
echo "--> Done <--"

echo -e ">> install python pips :) <<"
sudo apt install python3-pip
echo -e ">> DONE <<"

echo -e "--> pips <--"
python3 -m pip install selenium==3.141.0
python3 -m pip install requests==2.23.0
python3 -m pip install colorama==0.4.3
