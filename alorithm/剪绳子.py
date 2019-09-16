def find_max_res(l):
    if l<2:
        return 0
    if l==2:
        return 1
    if l==3:
        return 2
    
    res=[0,1,2,3]
    
    for i in (4,l):
        m=0
        for j in range(1,i//2):
            if m<res[j]*res[i-j]:
                m=res[j]*res[i-j]
        res.append(m)
        
    
    return res[-1]


