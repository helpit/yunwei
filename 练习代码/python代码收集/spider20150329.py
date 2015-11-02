#!/usr/bin/env python
import urllib2
content = urllib2.urlopen('http://mp3.baidu.com').read()
print content
