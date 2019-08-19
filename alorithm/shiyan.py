
def find_count(summ,num,k,ans,a,path):
    print('{0}----{1}'.format(id(path),path))
    print('{0}-----------{1}'.format(id(ans),ans))
    print('---------------------------{0}--{1}'.format(id(a),a))
    if len(path)==k:
        if sum(path)==summ:
            ans[0]=ans[0]+1
            a=a+1
            return
        else:
            return
        
    if len(num)==0 or len(path)>k:
        return
    find_count(summ,num[1:],k,ans,a,path+[num[0]])
    find_count(summ, num[1:], k, ans,a, path)

def find(summ,k):
    num=list(range(1,summ))
    ans,a=[0],0
    find_count(summ,num,k,ans,a,[])
    
    print(ans)


find(4,2)