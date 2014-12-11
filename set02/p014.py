# coding: utf-8

import re

tweets = map(lambda l: l.rstrip('\n'), open('../data/tweets.txt').readlines())

r = re.compile(u'\s*(@\w+?)\s'.encode('utf-8'))
for t in tweets:
  s = r.search(t)
  if s: print s.group(1)

