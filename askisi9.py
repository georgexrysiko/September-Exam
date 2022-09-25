def pair(lst,t):
    for i in lst:
        tmp = t-i
        if tmp in lst:
            lst.remove(i)
            lst.remove(tmp)
    return(lst)