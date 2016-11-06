#!/usr/bin/python
#-*- coding:UTF-8 -*-

import urllib

page=urllib.urlopen("http://localhost:8080/index")
html=page.read()
print html