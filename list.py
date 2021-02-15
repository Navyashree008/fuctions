list = []
i = 1
n = int(input("enter a number"))
while i <= n:
    num = int(input("enter no"))
    list.append(num)
    i+=1
list2 = []
i = 0
list2.append(list[i])
while i < len(list):
    list2.append(list2[i]+1)
    i+=1
print(list2)
if list == list2:
    print("true")
else: 
    print("false")

