num = [1,7,85,34,9,70]
print(num[0], num[-1])
sorted = num.sort()
print(sorted)
print(num.sort(reverse = True))
print(num.reverse())
num1 = [98,345]
num2 = num1.copy()
print(num2.append(num))

for i in num:
    print(i)
for index, n in enumerate(num):
    print(index,n)    
print([i**2 for i in num])        