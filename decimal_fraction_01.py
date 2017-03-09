import decimal
from fractions import Fraction


decimal.getcontext().prec = 2          #duas casas decimais

print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

f = Fraction(2,3)

print(f+1)









