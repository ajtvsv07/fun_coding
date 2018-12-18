max_out = -1


def max_path_sum(root):
    global max_out
    rcall(root)
    return max_out


def rcall(root):
    global max_out
    if not root:
        return -1

    root_val = root.val

    if root.left:
        left = max(0, rcall(root.left))
    else:
        left = 0

    if root.right:
        right = max(0, rcall(root.right))
    else:
        right = 0

    max_out = max(max_out, root_val+left+right)

    return root_val+max(left, right)

