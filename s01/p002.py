# coding: utf-8

f = open('../data/address.txt')
l = f.readline()

while l:
  print l.replace('\t',' ').rstrip('\n')
  l = f.readline()

