#这里有一个类属性laugh。在方法show_laugh()中，通过self.laugh，调用了该属性的值。
#还可以用相同的方式调用其它方法。方法show_laugh()，在方法laugh_100th中()被调用。
#通过对象可以修改类属性值。但这是危险的。类属性被所有同一类及其子类的对象共享。类属性值的改变会影响所有的对象。


class Human(object):
	laugh = 'hahahaha'
	def show_laugh(self):
		print self.laugh
	def laugh_100000th(self):
		for i in range(100000):
			self.show_laugh()
			
li_lei = Human()
li_lei.laugh_100000th()
