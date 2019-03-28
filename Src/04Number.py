import math
import random

var1 = 1
var2 = 10
print(var1,var2)
# del var1,var2
# print(var1,var2)

a = 2.6
int(a)
print(a)
print(int(a))

print(17 // 3) # 整数除法返回向下取整后的结果
print(17 % 3) # ％操作符返回除法的余数
print(7.0 // 2) # //得到的并不一定是整数类型的数，它与分母分子的数据类型有关系。
print(7.0 % 2)

print(math.ceil(4.1))
print(math.floor(4.7))

#################################################
print(random.choice(range(10)))

print(random.randrange(1,100,2)) #从 1-100 中选取一个奇数
print("randrange(100) : ", random.randrange(100)) # 从 0-99 选取一个随机数

print(random.random()) # 随机生成下一个实数，它在[0,1)范围内。

random.seed()
print ("使用默认种子生成随机数：", random.random())
random.seed(10)
print ("使用整数种子生成随机数：", random.random())
random.seed("hello",2)
print ("使用字符串种子生成随机数：", random.random())

list = [20, 16, 10, 5];
random.shuffle(list)
print("随机排序列表 : ", list)
random.shuffle(list)
print("随机排序列表 : ", list)

print("uniform(5, 10) 的随机浮点数 : ", random.uniform(5, 10))
float2 = round(random.uniform(7,14),2)
print("uniform(7, 14) 的随机浮点数 : ", float2)