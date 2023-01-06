#!/usr/bin/python3
"""
pascal test case
"""

result = []
temp = []
l = [1]
result.append(l)
l1 = [1,1]

result.append(l1)

#2
temp.append(1)
for i in range(len(result[-1]) - 1):
    temp.append(result[-1][i]+result[-1][i+1])
temp.append(1)

result.append(temp)
temp=[]

#3
temp.append(1)
for i in range(len(result[-1]) - 1):
    temp.append(result[-1][i]+result[-1][i+1])
temp.append(1)

result.append(temp)

#4
temp = []
temp.append(1)
for i in range(len(result[-1]) - 1):
    temp.append(result[-1][i]+result[-1][i+1])
temp.append(1)

result.append(temp)
print(result)
