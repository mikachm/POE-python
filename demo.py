x = 3
s = "Hello world"
print(s,x)
n = 3.14
print(f"ceci est le nombre ",(n))

def add(i,j):
    return i+j

print(add(3,2))

for i in range (10,20,2):
    print(i)

def isPrime(n):
    result = True
    if n<2:
        result = False
    else:
        for i in range(2,n):
            if n % i == 0:
                result = False
                break
    print(result)

for i in range(1,26):
    print(f"n= ",i)
    print(f" ----> ",(isPrime(i)))

l = [1,2,3,4,5,6,8,9]
i = 3
x = l[i]
l.append(99)
l.remove(5)
for i in l:
    print(i)