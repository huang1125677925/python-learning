def lpath(root, path):
    print('{0}-----{1}'.format(id(path),path))
    if root==[]:
        print('end------'+path)
        print(id(path))
    else:
        path += str(root[0])
        lpath(root[1:], path)

root=list(range(10))
s=''
lpath(root, s)