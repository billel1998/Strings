def removeduplicates(l):
    i = 0
    for i in l:
        j = i+1
        for j in l:
            if j == len(l):
                return l
            elif i == j:
                l.remove(j)


    return l
a = [1,2,1,3,4]
print(removeduplicates(a))
