# coding: utf-8

f = open('../data/address.txt')

cnt = 0
while f.readline():
  cnt += 1

print cnt

