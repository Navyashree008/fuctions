def maximum(a):
    if type(a) == list:
        i = 0
        max = 0
        while i < len(a):
            j = 0
            while j < len(a):
                if a[i] > max:
                    max = a[i]
                j+=1
            i+=1
        return max
    else:
        num = int(input("enter no"))
        list1 = []
        k = 1
        while k <= num:
            no = int(input("enter no"))
            list1.append(no)
            k+=1
        i = 0
        max = 0
        while i < len(list1):
            j = 0
            while j < len(list1):
                if list1[i] > max:
                    max = list1[i]
                j+=1
            i+=1
        return max
print(maximum(4))