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

    print(inorderMorrisTraversal(root))
    # print(preorderMorrisTraversal(root))