'''

'''

求树的最大深度
判断树是不是平衡二叉树
把树进行镜像



def reverse(root):
    if root is None:
        return
    if root.right or root.left:
        temp=root.right
        root.left=root.right
        root.right=temp
    
    reverse(root.right)
    reverse(root.left)
    
def check_same(root):
    
    return check_same_def(root,root)

def check_same_def(root1,root2):
    if root1.val!=root2.val:
        return False
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    
    return check_same_def(root1.left,root2.right) and check_same_def(root1.right,root2.left)

def find_max_deepth(root):
    if root is None:
        return 0
    
    left=1+find_max_deepth(root.left)
    right=1+find_max_deepth(root.right)
    
    return max(left,right)