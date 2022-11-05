class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def preorder(root):
    if root == None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")



### inorder morristraversal
def getRightNode(leftNode, curr):
    while leftNode.right != None and leftNode.right != curr:
        leftNode = leftNode.right
    return leftNode
def inorderMorrisTraversal(root):
    ans = []
    curr = root
    while curr != None:
        leftNode = curr.left
        # if left node is null -> print current node -> goto right node
        if leftNode == None:
            ans.append(curr.data)
            curr = curr.right
        # find rightMostNode. after that here will be 2 scenarios (create a theard, cut down thread)    
        else:  
            rightMostNode = getRightNode(leftNode, curr)
            if rightMostNode.right == None:    # create thread
                rightMostNode.right = curr
                curr = curr.left
            else:    # cut down thread
                rightMostNode.right = None
                ans.append(curr.data)
                curr = curr.right
                
    return ans


def preorderMorrisTraversal(root):
    ans = []
    curr = root
    while curr != None:
        leftNode = curr.left
        # if left node is null -> print current node -> goto right node
        if leftNode == None:
            ans.append(curr.data)
            curr = curr.right
        # find rightMostNode. after that here will be 2 scenarios (create a theard, cut down thread)    
        else:  
            rightMostNode = getRightNode(leftNode, curr)
            if rightMostNode.right == None:    # create thread
                rightMostNode.right = curr
                ans.append(curr.data)
                curr = curr.left
            else:    # cut down thread
                rightMostNode.right = None
                curr = curr.right
                
    return ans 
    






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

    # preorder(root)
    # inorder(root)
    # postorder(root)

    # print(inorderMorrisTraversal(root))
    # print(preorderMorrisTraversal(root))
    print(minCameraCover(root))