def sum_3(a,b,c):
    total = a+b+c
    avg = total//3
    print(total)
    return avg
a = int(input("enter no1"))
b = int(input("enter no2"))
c = int(input("enter no3"))
z = sum_3(a,b,c)
print(z)