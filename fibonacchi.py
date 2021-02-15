def fibonacci(num):
    first = 0
    second = 1
    temp = 0
    i = 0
    while i< num:
        print(first)
        temp = first+second
        first = second
        second = temp
        i+=1
num = int(input("enter number"))
fibonacci(num)