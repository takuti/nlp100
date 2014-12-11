# coding: utf-8

import re

tweets = map(lambda l: l.rstrip('\n'), open('../data/tweets.txt').readlines())

r = re.compile(u'\s*(@\w+?)\s'.encode('utf-8'))
for t in tweets:
  i = 0
  while True:
    m = r.search(t, i)
    if m:
      print m.group(1)
      i = m.end()
    else:
      break


