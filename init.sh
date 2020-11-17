#!/bin/bash
source ./ENV/bin/activate 
pip3 install -r requirements.txt > /dev/null
python3 main.py
