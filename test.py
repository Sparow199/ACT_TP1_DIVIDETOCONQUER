#!/usr/bin/python
# coding: utf8

def read(file):
    with open(file, 'rb') as f:
        lines = f.readlines()
        l,h = lines[0].split()
        n = lines[1]
        points = [tuple(x.split()) for x in lines[2:]]
    return int(l), int(h), int(n), [(int(x[0]), int(x[1])) for x in points]

if __name__== "__main__":
    print read('donneesPourTests/ex500_7616')
