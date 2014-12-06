# coding: utf-8

f = open('../data/address.txt')
l = f.readline()

col1 = []
col2 = []
while l:
  row = l.rstrip('\n').split('\t')
  col1.append(row[0])
  col2.append(row[1])
  l = f.readline()

f.close()

open('./col1.txt', 'w').write('\n'.join(col1) + '\n')
open('./col2.txt', 'w').write('\n'.join(col2) + '\n')
