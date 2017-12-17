#!/usr/bin/python
import cProfile
import pstats
from asdf import doit

cProfile.run("doit('input.txt')", 'restats')
p = pstats.Stats('restats')
p.sort_stats('cumulative').print_stats(10)
