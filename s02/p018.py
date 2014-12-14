# coding: utf-8

import re

tweets = map(lambda l: l.rstrip('\n'), open('../data/tweets.txt').readlines())

r = re.compile(u'仙台市[一-龠]+[\-0-9]+'.encode('utf-8'))
for t in tweets:
  i = 0
  while True:
    m = r.search(t, i)
    if m:
      print m.group(0)
      i = m.end()
    else:
      break


