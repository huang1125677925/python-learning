class Solution:
    def reconstructQueue(self, people):
        people.sort(key = lambda x: [-x[0], x[1]])
        res = []
        for p in people:
            res.insert(p[1], p)
        print(res)
        return res
	
from collections import deque
a=deque()

	
	
if __name__ == '__main__':
    import numpy as np
    import pandas as pd
    data=np.random.normal(1,1,100)
    
    d = pd.DataFrame(data=data,columns=['data'])
    d['feature']=pd.cut(d['data'],bins=10)
    
    
    bindata=d.groupby(by='feature').size()
    
    print(bindata)

    import matplotlib.pyplot as plt

    rng = np.random.RandomState(10)  # deterministic random data
    a = np.hstack((rng.normal(size=1000),
                   rng.normal(loc=5, scale=2, size=1000)))
    _ = plt.hist(data, bins=[-3,-2,-1,0,1,2,3,4])  # arguments are passed to np.histogram
    plt.title("Histogram with 'auto' bins")

    plt.show()