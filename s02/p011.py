# coding: utf-8

import re

tweets = map(lambda l: l.rstrip('\n'), open('../data/tweets.txt').readlines())

r = re.compile(u'拡散希望'.encode('utf-8'))
for t in tweets:
  if r.search(t): print t
