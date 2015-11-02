#!/usr/bin/env python
# import a as b  引入模块A，并将模块A生命名
# from a import function1  从模块A中引入function1对象。调用A中对象时，我们不用再说
#  明模块，即直接使用function1,而不是a.function1.
# from a import * 从模块A中引入所有对象，调用A中对象时，我们不用再说明模块，即直接使用
# 对象，而不是a.对象。






import first

for i in range(100000):
	first.laugh()
