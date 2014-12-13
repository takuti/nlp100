# coding: utf-8

import re

tweets = map(lambda l: l.rstrip('\n'), open('../data/tweets.txt').readlines())

r = re.compile(u'[一-龠]+?(くん|ちゃん|さん|氏)'.encode('utf-8'))
for t in tweets:
  i = 0
  while True:
    m = r.search(t, i)
    if m:
      print m.group(0)
      i = m.end()
    else:
      break


