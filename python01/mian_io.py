#!/usr/bin/python
#coding=utf-8

import os


file=open("output.txt", "r+")
# file.write("Hello World\n")
# file.writelines("你好，世界！\n")
# file.seek(0,0)
s=file.readline();
# s=file.next()
print s
s1=file.next()
print s1
print os.getcwd()
os.chdir("D:\Projects\codes")
print os.getcwd()
file.close()

