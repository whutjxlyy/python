#!/usr/bin/python
#coding=utf-8

import types


if __name__=="__main__":
    print "###########################"
    print
    print
    ##################################
    ##################################

    # li=[1,5,7,4,3,2,2,4]
    #
    # otherLi=[num*3+3 for num in li]
    #
    # print li
    # print otherLi

    li=[]
    list=dir(li)
    method=[m for m in list if callable(getattr(list,m))]
    print method















    ##################################
    ##################################
    print
    print
    print "###########################"
