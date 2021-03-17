a = [ 1 -i for i in  range(1, 11, 1)]

print(a)

b = [ 4**x for x in range(8)]
print(b)

c = [y for y in b if y % 2 == 0]
print(c)
