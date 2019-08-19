# import pandas as pd
# import sys
# d=list(range(100000))
#
# print(sys.getsizeof(d))
#
# dd=pd.DataFrame(data=d)
#
# print(sys.getsizeof(dd))


a=range(100)

b=(chr(x) for x in a)


print([x for x in b])