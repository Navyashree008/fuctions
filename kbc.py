q = ['1q','2q','3q','4q']
op = [['a','b','c','d'],['a','b','c','d'],['a','b','c','d'],['a','b','c','d']]
sol = ['b','a','c','d']

#question function
def question(i):
    print(q[i])
    return(op[i])
# print(question(i))

# 50_50 function
def 50_50():
    import random
    wrong = [['a','c','d',],['b','c','d'],['a','b','d'],['a','b','c']]
    random_letter = random.choice(wrong[i])
    my_list = [random_letter,sol[i]]
    random.shuffle(my_list)
    return my_list
ans = input("enetr answer")
if ans == sol[i]:
    i+=1
    continue

#answer function
def answer(a):
    if user == sol[i]:
        print("its correct lets move forford")
        i+=1
    elif user == "50-50":
        print(50_50())



# # final answer
# def final_answer(ans):
#     if ans == sol[i]
i = 0
while True:
    print(question(i))
    user = input("enter your option")
    print(answer(user))