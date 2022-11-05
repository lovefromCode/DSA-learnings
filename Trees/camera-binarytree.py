class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data



###----- Imp... cameras in trees
def helperCamera(root, ans):
    # base case
    if root == None:
        return 1

    lc = helperCamera(root.left, ans)
    rc = helperCamera(root.right, ans)

    # if atleast one child is not monitored, we need to place a camera at
    if lc == 0 or rc == 0:
        ans.append(root.data)
        return 2
    # if atleast 1 child has camera, the current node is monitored
    elif lc == 2 or rc == 2:
        return 1
    # if both children are monitored but have no camera, we don't need to place at its parent node at higher level. (if lc == 1 and rc == 1)
    elif lc == 1 and rc == 1:
        return 0

    # return -1
        
        
    
## -------
# have camera - 2
# monitored - 1
# not monitored - 0
def minCameraCover(root):
    ans = []
    if helperCamera(root, ans) == 0:     # if root isnot monitored. we need to place additional camera at root
        ans.append(root.data)
    return ans


if __name__ == '__main__':
    root = Node(100) 
    root.left = Node(50)
    root.right = Node(60)
    root.left.left = Node(20)
    root.left.right = Node(-10)
    root.right.left = Node(13)
    root.right.right = Node(16)
    root.left.left.right = Node(-40)

    
    print(minCameraCover(root))