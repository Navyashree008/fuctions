def length_of_string(a,b):
    if len(a) == len(b):
        return a,b
    elif len(a) > len(b):
        return a
    else:
        return b
a = input("enter any string")
b = input("enter another string")
print(length_of_string(a,b))