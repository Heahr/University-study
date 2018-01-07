a = input('a = ')

a = int(a)

sec = a % 60
sec = int(sec)

b = a // 60
b = int(b)

m = (b % 60)//60
m = int(m)

h = b // 60
h = int(h)

print(h,m,sec)

#3600은 안쓸것.
