def prime(a):
    if a > 0:
        i = 2
        while i < a:
            if a % i == 0:
                return "not a prime number"
            i+=1
        return "its a prime number"
a = int(input("enter number"))
print(prime(a))       