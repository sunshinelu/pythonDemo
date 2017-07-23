# Numerical Stability

a = 1000000000
for i in range(1000000): # in python2 using xrange
    a = a + 1e-6
print(a - 1000000000)
# 0.95

b = 1
for i in range(1000000):
    b = b + 1e-6
print(b - 1)
# 当将a设置为1时，命名为b，此时print的值更接近1.