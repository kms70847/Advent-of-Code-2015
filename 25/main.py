import re

with open("input") as file:
    row, col = map(int, re.findall("\d+", file.read()))

p = (row-1) + (col-1)
q = p - (row - 1)
idx = (p**2 + p)//2 + q

x = 20151125
for i in range(idx):
    x = (x * 252533) % 33554393
print(x)