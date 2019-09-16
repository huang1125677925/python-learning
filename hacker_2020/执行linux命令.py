import os
# os.system('ping 192.168.2.30')
cmd='ping 192.168.2.30'

textlist = os.popen(cmd)


for l in textlist:
    print(l)
