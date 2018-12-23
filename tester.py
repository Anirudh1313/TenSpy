from tenspy import *

on = ones((2, 4, 4))
print(on)

print(reshape(on, (2, 2, 8)))

print(ones((1, 1, 1, 1, 1, 1)))

k = tenspy([1,3,2])
k._pri = 2
print(k)

print(k._tenspy__build_ones(1,3,(2,2,2,2)))

#print(k.ten)
#print(k.dtype)
