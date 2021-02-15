def show_numbers(num):
    # i = 1
    # while i <= limit:
    if num%2 == 0:
        return num,"is even"
    else:
        return num ,"is odd"
        # i+=1
j=1
while j<=10:
    print(show_numbers(j))
    j=j+1

