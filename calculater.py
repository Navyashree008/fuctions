def sum(a,b):
    total = a+b
    return total
def sub(a,b):
    total = a-b
    return total
def multiple(a,b):
    total = a*b
    return total
def div(a,b):
    total = a//b
    return total

def calsi(a = int(input("enter no1")),b = int(input("enter no2")),c = input("enter operator")):
    if c == "+":
        return(sum(a,b))
    elif c=="-":
        return sub(a,b)
    elif c == "*":
        return multiple(a,b)
    else:
        return div(a,b)
# a = int(input("enter any number"))
# b = int(input("enter any other number"))
# c = input("enter any operator")
print(calsi())
