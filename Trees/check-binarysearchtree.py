class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


## 1. Brute Force Approach
# We need to check is the left subtree of a node contains any element greater than the node’s value and whether the right subtree of a node contains any element smaller than the node’s value.
# We shall design two helper functions getMin(root) and getMax(root) which will get the minimum and maximum values of the tree with a given root. Then we will check :
# If the node’s value is greater than the maximum value in the left subtree or not
# The node’s value is lesser than the minimum value in the right subtree or not. Basically, we will check if this expression holds true or not: getMax(root.left) < root.val < getMin(root.right)



## method 2 - min and max range
import sys
def bstUtils(root, min, max):
    if root == None:
        return True
    
    if root.data < min or root.data > max:
        return False

    if bstUtils(root.left, min, root.data-1) and bstUtils(root.right, root.data+1, max):
        return True

    return False

def isBST(root):
    return bstUtils(root, -sys.maxsize, sys.maxsize)




## method 3 - ## inorder traversal of binary search tree is sorted in nature. [space - O(n)]  
def inorder(root, ans):
    if root == None:
        return
    inorder(root.left, ans)
    ans.append(root.data)
    inorder(root.right, ans)
   
def checkBST(root):
    # find inorder, store in list, then check list is sorted or not.
    ans = []
    inorder(root, ans)
    return ans == sorted(ans)




# optimaized without space - like inorder fashion
def helper(root, prev):
    if root == None:
        return True
    
    if helper(root.left, prev) == False:        # check left child is BST or not
        return False

    if prev != None and prev.data >= root.data:     # check before going to right subtree.
        return False

    prev = root

    if helper(root.right, prev) == False:       # check right child is BST or not
        return False

    return True         # if both subtree are true.

def inorder_fashion(root):
    prev = None
    return helper(root, prev)





# morris traversal 



if __name__ == '__main__':
    root = Node(10) 
    root.left = Node(7)
    root.left.right = Node(5)
    root.right = Node(20)
    root.right.left = Node(13)
    root.right.right = Node(30)


    # print(isBST(root))
    # print(checkBST(root))
    print(inorder_fashion(root))




