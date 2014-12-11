# coding: utf-8

import sys

if len(sys.argv) != 2:
  print 'One commandline argument is required.'
  quit()
n = int(sys.argv[1])

f = open('../data/address.txt')
l = f.readline()

cnt = 0
while l and cnt < n:
  print l.rstrip('\n')
  cnt += 1
  l = f.readline()
f.close()
