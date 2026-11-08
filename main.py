#from model import Transaction

#t = Transaction("expense", "food", 1500, "lunch")

#t = Transaction("expense", "food", 1500)
#print(t)
from model import Transaction

t = Transaction("expense", "food", 1500, "lunch")
t2 = Transaction("income", "allowance", 50000)
print(t)
print(t2)
print(t.amount)