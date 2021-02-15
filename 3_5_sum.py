def multiple(limit):
    i = 1
    sum = 0
    while i <= limit:
        if i % 3 == 0 and i % 5 == 0:
            sum = sum+i
        i+=1
    return(sum)
z = multiple(30)
print(z)