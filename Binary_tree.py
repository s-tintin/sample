
class NewNode:

    def __init__(self, data):
        self.key = data
        self.rightChild = None
        self.leftChild = None

def inorder(node):
    if not node:
        return
    inorder(node.leftChild)
    print(node.key, end = " ")
    inorder(node.rightChild)

def insert(node, value):
    queue = []
    queue.append(node)

    while len(queue):
        temp = queue.pop(0)

        if not temp.leftChild:
            temp.leftChild = NewNode(value)
            break
        else:
            queue.append(temp.leftChild)

        if not temp.rightChild:
            temp.rightChild = NewNode(value)
            break
        else:
            queue.append(temp.rightChild)

def deletion_deepest(root, del_node):
    queue = []
    queue.append(root)

    while len(queue):
        temp = queue.pop(0)

        if temp == del_node:
            temp = None
            return
        if temp.rightChild:
            if temp.rightChild == del_node:
                temp.rightChild = None
                return
            else:
                queue.append(temp.rightChild)
        if temp.leftChild:
            if temp.leftChild == del_node:
                temp.leftChild = None
                return
            else:
                queue.append(temp.leftChild)

def deletion(root, del_value):
    if not root:
        return None
    if root.leftChild is None and root.rightChild is None:
        if root.key == del_value:
            return None
        else:
            return root

    queue = []
    key_node = None
    queue.append(root)

    while len(queue):
        temp = queue.pop(0)

        if temp.key == del_value:
            key_node = temp
        if temp.leftChild:
            queue.append(temp.leftChild)
        if temp.rightChild:
            queue.append(temp.rightChild)

    if key_node:
        x = temp.key
        deletion_deepest(root, temp)
        key_node.key = x

    return root


if __name__ == '__main__':
    root = NewNode(10)
    root.leftChild = NewNode(11)
    root.leftChild.leftChild = NewNode(7)
    root.leftChild.rightChild = NewNode(12)
    root.rightChild = NewNode(9)
    root.rightChild.leftChild = NewNode(15)
    root.rightChild.rightChild = NewNode(8)
    print("The tree before the deletion:")
    inorder(root)
    key = 11
    root = deletion(root, key)
    print()
    print("The tree after the deletion;")
    inorder(root)