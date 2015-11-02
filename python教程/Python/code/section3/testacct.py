
from bankaccount import *
# First a standard BankAccount</SPAN>
a = BankAccount(500)
b = BankAccount(200)
a.withdraw(100)
# a.withdraw(1000)
a.transfer(100,b)
print "A = ", a.checkBalance()
print "B = ", b.checkBalance()

# Now an InterestAccount</SPAN>
c = InterestAccount(1000)
c.deposit(100)
print "C = ", c.checkBalance()

# Then a ChargingAccount</SPAN>
d = ChargingAccount(300)
d.deposit(200)
print "D = ", d.checkBalance()
d.withdraw(50)
print "D = ", d.checkBalance()
d.transfer(100,a)
print "A = ", a.checkBalance()
print "D = ", d.checkBalance()

# Finally transer from charging account to interet one
# The charging one should charge and the interest one add
# interest</SPAN>
print "C = ", c.checkBalance()
print "D = ", d.checkBalance()
d.transfer(20,c)
print "C = ", c.checkBalance()
print "D = ", d.checkBalance()

raw_input('Hit a key to exit')
