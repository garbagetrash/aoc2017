#!/bin/bash

python -m cProfile -o profile.dat ./part2.py input.txt
./print_profile.py
