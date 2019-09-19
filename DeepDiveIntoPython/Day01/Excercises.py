# 1)
a,b,c = 4,2,5
result1 = a*c / 3
result2 = b-2
print(result1 >= result2)

print(8 == 8.0)

print (8 == '8.0')

print(True and False or False)

print((True or False) and False)

print(True and (False or not True))

x,y,z = 1,4,14
print(x<=1 or y>1 and z<1) # result is true, T or T and F -> T or (T and F) -> T or F -> T

#s1
time, velocity = 5,3
temp = time
time = velocity
velocity = temp
print(time,velocity)
#s2
time, velocity = 5,3
time, velocity = velocity,time
print(time,velocity)
#s3
time, velocity = 5,3
time = time + velocity
velocity = time - velocity
time = time - velocity
print(time,velocity)
