# coding: utf-8

from collections import Counter
from operator import itemgetter

lines = map(lambda l: l.rstrip('\n'), open('col2.txt').readlines())
cnt = Counter(lines)

for l, c in (sorted(cnt.items(), key=itemgetter(1,0), reverse=True)):
  print l

