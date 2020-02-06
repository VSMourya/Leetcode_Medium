

def flatten(root):
    """
    Do not return anything, modify root in-place instead.
    """

    if not root:
        return

    stack = [root]

    while stack:

        currNode = stack.pop()

        if currNode.right:
            stack.append(currNode.right)

        if currNode.left:
            stack.append(currNode.left)

        if stack:
            currNode.right = stack[-1]

        currNode.left = None

