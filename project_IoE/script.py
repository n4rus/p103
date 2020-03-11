#!/usr/bin/python

print """#!/bin/bash

#Python script to test skills within bash and emacs
"""
print "mkdir new_dataset"

print """cp script.py new_dataset
cp out.sh new_dataset
chmod +x ./out.sh
chmod +x ./script.py
./script.py > out.sh
cd new_dataset
./out.sh
"""
