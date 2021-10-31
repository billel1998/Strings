def removeevennumbers(l):
    for i in l:
        if i % 2== 1:
            l.remove(i)
    return l
a =[1,2,3,4]
print(removeevennumbers(a))



