def print_circle(m,n,d):
    if m==1 and n==1:
        return d[0][0]
    
    start=0
    
    while(m>start*2 and n>start*2):
        
        print_number(m,n,d,start)
        
        start+=1
    
def print_number(m,n,d,start):
    endx=n-1-start
    endy=m-1-start
    
    for i in range(start,endx+1):
        print(d[start][i])
        
    if start<endy:
        for j in range(start+1,endy+1):
            print(d[j][endx])
    
    if start<endy and start<endx:
        for i in range(endx-1,start-1,-1):
            print(d[endy][i])
            
    
    if start<endy-1 and start<endx:
        for i in range(endy-1,start,-1):
            print(d[i][start])