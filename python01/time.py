#-*- coding:UTF-8 -*-
import time;
import calendar;

#测试time
tick=time.time()
print "time stmps",tick
localtime=time.localtime(tick)
print "当前时间为：",time.asctime(localtime)

print ""

#测试calendar
cal=calendar.month(2016,10)
print cal