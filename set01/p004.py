# coding: utf-8

f1 = open('col1.txt')
f2 = open('col2.txt')
l1 = f1.readline()
l2 = f2.readline()

while l1 and l2:
  print '%s\t%s' % (l1.rstrip('\n'), l2.rstrip('\n'))
  l1 = f1.readline()
  l2 = f2.readline()

