# coding: utf-8

import re

tweets = map(lambda l: l.rstrip('\n'), open('../data/tweets.txt').readlines())

r = re.compile(u'(.+?) (RT|QT).*$'.encode('utf-8'))
for t in tweets:
  m = r.match(t)
  if m: print m.group(1)

