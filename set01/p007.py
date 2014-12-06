# coding utf-8

f = open('col1.txt')
l =  f.readlines()

print len(set(l))
