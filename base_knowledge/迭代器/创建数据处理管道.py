#假设处理的数据量太大，无法一下放到内存中，可以通过这种方法来解决

import os,fnmatch,gzip,bz2,re

def gen_find(filepat,top):
    for path,dirlist,filelist in os.walk(top):
        print(path,dirlist)
        for name in fnmatch.filter(filelist,filepat):
            yield os.path.join(path,name)
            print(os.path.join(path,name))
            

def
        
        
if __name__ == '__main__':
    gen_find('*.py','/Users/huangchuang/Documents/GitHub/linux_python')
    import datetime

    datetime.datetime.strptime('2019-09-24 15:55:35')
    