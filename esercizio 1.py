from math import radians, sqrt
cateto1 = 10.123
cateto2 = 30.456

ipotenusa = sqrt(cateto1**2 + cateto2**2)
print (ipotenusa) 


import math
ϕ1 = radians(59.9)
λ1 = radians(10.8)
ϕ2 = radians(49.3)
λ2 = radians(-123.1)
raggio = 6371

d = 2*raggio*math.asin(sqrt(math.sin(0.5*(ϕ2 - ϕ1))**2 + math.cos(ϕ1)*math.cos(ϕ2)*math.sin(0.5*(λ2 - λ1))**2))
print (d)