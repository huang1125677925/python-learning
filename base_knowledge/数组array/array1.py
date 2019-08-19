from array import array
from random import random

# floats=array('d',(random() for i in range(10**7)))
#
# fp=open('floats.bin','wb')
# floats.tofile(fp)
#
# fp.close()


f=open('floats.bin','rb')

floats=array('d')
floats.fromfile(f,10**7)

f.close()

print(floats[-1])
