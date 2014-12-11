# coding: utf-8

import re

tweets = map(lambda l: l.rstrip('\n'), open('../data/tweets.txt').readlines())

r = re.compile(u'.*なう$'.encode('utf-8'))
for t in tweets:
  if r.match(t): print t

