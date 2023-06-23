s = dict()
s1 = dict()

for i in range(10, -6, -1):
    s = {i:i**i}
    s1.update(s)
    
print(s1)
