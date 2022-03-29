import math
r = int(input("반지름 입력: "))
S = 4*(3.14*math.pow(r,2))
V = 3/4*(3.14*math.pow(r,3))
print("겉면적: ",float(S))
print("부피: ",float(V))