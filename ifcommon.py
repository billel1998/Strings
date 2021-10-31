def ifcommon(l,a):
    i = 0
    for i in l:
        for j in a:
            if i == j:
                return "they have at least one common element"
    return "the don't have any common element"
c =[1,2,3]
b =[4,5,3]
print(ifcommon(c,b))


