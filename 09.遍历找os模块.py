#!/usr/bin/env python
# encoding: utf-8

cnt=0
for item in [].__class__.__base__.__subclasses__():
    try:
        if 'os' in item.__init__.__globals__:
            print cnt,item
        cnt+=1
    except:
        print "error",cnt,item
        cnt+=1
        continue