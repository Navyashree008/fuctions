# def segregation(a):
#     num = []
#     name = []
#     list = []
# a = input("give user input of your wish:")
# a = " 'poonam' , 3 , [1,2,3,4,5] , 'r' , 'crazy' , 7 , 'navya' , 'p' , ['a','b','c'] "
# print(len(a))

a = " 'poonam' , 3 , [1,2,3,4,5] , 'r' , 'crazy' , 7 , 'navya' , 'p' , ['a','b','c'] "
print(len(a))
num = []
name = []
list1 = []
i = 0
while i < len(a):
    if a[i] == int:
        num.append(a[i])
    elif a[i] == str:
        name.append(a[i])
    elif a[i] == list:
        list1.append(a[i])
    i+=1
print(num)
print(name)
print(list1)