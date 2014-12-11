# coding: utf-8

import re

tweets = map(lambda l: l.rstrip('\n'), open('../data/tweets.txt').readlines())

r = re.compile(u'\s*(@\w+?)\W'.encode('utf-8'))
for t in tweets:
  i = 0
  sub_t = t
  while True:
    m = r.search(t, i)
    if m:
      uid = m.group(1)
      sub_t = sub_t.replace(uid, '<a href=\"https://twitter.com/#!/%s\">%s</a>' % (uid[1:], uid))
      i = m.end()
    else:
      break
  print sub_t


