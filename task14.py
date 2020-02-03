def stepPerms(n):
    l = [1,2,4]

    for i in range(1, n):
        s = sum(l[-3:])
        l.append(s)
    
    return l[n-1]
