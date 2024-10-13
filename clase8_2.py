a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a[0]
# Devuelven el mismo espacio en memoria, con lo cual si modificas "a" se ve afectado "b" también
print(id(a))
print(id(b))
c = a[:]
print(id(a))
print(id(b))
print(id(c))
a.append(6)
print(a)
print(b)
print(c)