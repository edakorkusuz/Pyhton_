'''
  
  Yarıçapı verilen bir dairenin alan ve çevresinin hesaplayınız.

'''

import math

r = float(input("Yarıçap giriniz: "))

alan = math.pi * (r ** 2)
cevre = 2 * math.pi * r

print('Alan:', alan, "   ", 'Çevre:', cevre)