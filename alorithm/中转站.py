def dfs(self,index,res,path,l):
    if index==4:
        if sum(res)==0:
            path.append(res)
        return
    
    
    
    dfs(self,index+1,res+[l[index][0]],path,l)
    dfs(self,index+1,res+[l[index][1]],path,l)
    
    


def mian(n):
    temp=[0,1,1]
    if n<3:
        return temp[n]
    
    while len(temp)<n+1:
        temp.append(sum(temp[-3:]))
        
    return temp[n]


def bit1(bits):
    bit=''.join(list(map(str,bits)))
    
    if len(bit)==0:
        return False
    if len(bit)==1:
        if int(bit) == 0:
            return True
        else:
            return False
    
    if len(bit)==2:
        if int(bit) in [10,11,1]:
            print('就是这')
            return True
        else:
            return False
    
    while len(bit)>2:
        if bit[:2] in ['10','11']:
            bit=bit[2:]
        elif bits[0]=='0':
            bit=bit[1:]
    
    bit1(list(map(int,list(bit))))
    
class Solution:
    def numberOfArithmeticSlices(self, A) -> int:
        count = 0
        for s in range(0,len(A)-2):
            d = A[s + 1] - A[s]
            for e in range(s+2,len(A)):
                i = 0
                for i in range(s+2,e+1):
                    if A[i] - A[i - 1] != d:
                        i=i-1
                        break
                if i >= e:
                    count+=1
        return count


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, nums):
        t=[1 if nums[x]-nums[x-1]==1 else 0 for x in range(1,len(nums))]
        tindex=[]
        flag=False
        d=10000
        for i in t:
            if i==1:
                flag=True
            elif i==0:
                if d==10000:
                    continue


class MagicDictionary:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
    
    def buildDict(self, dict) -> None:
        """
        Build a dictionary through a list of words
        """
        self.data += dict
    
    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        if word in self.data:
            return False
        l = len(word)
        L = [len(x) for x in self.data]
        if l not in L:
            return False
        for item in self.data:
            if l != len(item):
                continue
            else:
                for i in range(l):
                    word,item=list(word),list(item)
                    a,b=word[:i]+word[i+1:],item[:i] +item[i+1:]
                    if a==b:
                        return True
        
        return False


class Solution:
    def nextGreaterElements(self, nums):
        temp=[]
        for i in range(len(nums)):
            s=nums[i+1:]+nums[:i]
            t = []
            for j in s:
                if j>nums[i]:
                    t.append(j)
            if t==[]:
                temp.append(-1)
            else:
                temp.append(t[0])
        
        return temp
        

print(Solution().nextGreaterElements([1,2,1]))
        

            
                
    


    
# path=[]
# res=[]
# index=0
# l=[[ 0, 0],[0,0],[0, 0],[ 0, 0]]
# dfs(index,res,path,l)
# print(len(path))