# coding: utf-8

from operator import itemgetter

lines = map(lambda l: l.rstrip('\n').split('\t'), open('../data/address.txt').readlines())

for l in sorted(lines, key=itemgetter(1)):
  print '%s\t%s' % (l[0], l[1])

