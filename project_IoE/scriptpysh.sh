#!/bin/bash

rm -dR new_dataset
rm out.sh
./script.py > out.sh
chmod +x out.sh
