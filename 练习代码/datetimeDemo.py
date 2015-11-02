#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import datetime
#t = datetime.datetime(2012,9,3,21,30)
#print(t)

import datetime
t      = datetime.datetime(2012,9,3,21,30)
t_next = t_next = datetime.datetime(2012,9,5,23,30)
delta1 = datetime.timedelta(seconds = 600)
delta2 = datetime.timedelta(weeks = 3)
print(t + delta1)
print(t + delta2)
print(t_next - t)
