class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# naive approach O(n^2)
def height(root):
    if root is None:
        return 0

    lh = height(root.left)
    rh = height(root.right)
    
    # use the larger one
    if lh > rh:
        return lh+1
    else:
        return rh+1

def helperTraversal(root, level):
    if root == None:
        return
    if level == 1:
        print(root.data, end=" ")
    if level > 1:
        helperTraversal(root.left, level-1)
        helperTraversal(root.right, level-1)

def levelOrderTraversal(root):
    # find height then run a loop and print node at every level
    for i in range(1, height(root)+1):
        helperTraversal(root, i)



def printLevelOrderTraversal(root):
    if root is None:
        return

    queue = []
    queue.append(root)
    while(len(queue) > 0):
        # print front of queue and remove it from queue
        print(queue[0].data, end=" ")
        popNode = queue.pop(0)
 
        # enqueue left child and right child
        if popNode.left is not None:
            queue.append(popNode.left)
        if popNode.right is not None:
            queue.append(popNode.right)


if __name__ == '__main__':
    root = Node(10) 
    root.left = Node(5)
    root.right = Node(6)
    root.left.left = Node(20)
    root.left.right = Node(10)
    root.right.left = Node(13)
    root.left.left.right = Node(-4)

    levelOrderTraversal(root)
    printLevelOrderTraversal(root)
