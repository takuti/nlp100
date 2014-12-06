# coding: utf-8

import sys

if len(sys.argv) != 2:
  print 'One commandline argument is required.'
  quit()
n = int(sys.argv[1])

f = open('../data/address.txt')
l = f.readlines()
f.close()

tail = l[len(l)-n:]
for t in tail:
  print t.rstrip('\n')
