def find_max_value():
    m,n=5,8
    d=[[0 for _ in range(m+1)]for _ in range(n+1)]
    
    for i in range(1,n+1):
        for v in range(w[i],V+1):
            d[i][v]=max(d[i-1][v],d[i-1][v-w[i]]+c[i])
            
    
    return d[n][m]


def find_max_value1():
    m, n = 5, 8
    d = [0 for _ in range(m + 1)]
    # 用一维数组的话必须是逆序
    for i in range(1, n + 1):
        for v in range(V, w[i]-1,-1):
            d[i][v] = max(d[v], d[v - w[i]] + c[i])
    
    return d[n][m]


    
    