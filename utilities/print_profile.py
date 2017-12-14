#!/usr/bin/python

import pstats
p = pstats.Stats('profile.dat')
p.sort_stats('cumulative').print_stats(10)
