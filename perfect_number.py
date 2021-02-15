def perfect(a):
    i = 1
    sum = 0
    while i < a:
        if a % i == 0:
            sum = sum+i
        i+=1
    if sum == a:
        print(a)
k = 1
while k <= 100:
    result = perfect(k)
    k+=1
