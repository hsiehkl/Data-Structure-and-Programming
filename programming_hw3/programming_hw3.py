############################################
#   107-1 Data Structure and Programming
#   Programming Assignment #3
#   Instructor: Pei-Yuan Wu
############################################

# Do not import any other library
import sys

# **********************************
# *  TODO                          *
# **********************************

class Node:
    def __init__(self, data,left=None,right=None):
        self.left = left
        self.right = right
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    # Preorder traversal
    # Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    # Postorder traversal
    # Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

def isValidPost(num_list, tree):

    if len(num_list) == 1:
        tree.insert(num_list[0])
        return True
    
    root = num_list.pop()
    tree.insert(root)

    split_index = 0

    for i in range(len(num_list)):
        if num_list[i] > root:
            break
        split_index = i + 1

    left_list = num_list[:(split_index)]
    right_list = num_list[(split_index):]

    for num in right_list:
        if num < root:
            return False

    left = True
    if len(left_list) > 0:
        left = isValidPost(left_list, tree)   

    right = True
    if len(right_list) > 0:
        right = isValidPost(right_list, tree)

    return left and right

# This function is for checking if a sequence can be a preorder of BST or not.
# if yes, return the postorder traversal of the BST.
# if not, return '-'.
def preorder_check(input_string):
    
    str_arr = input_string.split(",")
    node = Node(int(str_arr[0]))
    insert_arr = str_arr[1:]

    for i in insert_arr:
        node.insert(int(i))

    preorder = node.PreorderTraversal(node)
    preorder = list(map(str, preorder))

    if str_arr == preorder:
        postorder = node.PostorderTraversal(node)
        answer = ",".join(map(str, postorder))
        return answer
    else:
        return '-'

# This function is for checking if a sequence can be a postorder of BST or not.
# if yes, return the preorder traversal of the BST.
# if not, return '-'.
def postorder_check(input_string):

    str_arr = input_string.split(",")
    int_arr = list(map(int, str_arr))
    tree = Node(int_arr[(len(int_arr) - 1)])

    isValid = isValidPost(int_arr, tree)

    if isValid:
        preorder = tree.PreorderTraversal(tree)
        answer = ",".join(map(str, preorder))
        return answer
    else:
        return '-'

'''
Feel free to add more functions here
'''

# **********************************
# *  Do NOT modify the code below  *
# **********************************
if __name__ == '__main__':
    # 1. Check the command line arguments
    if len(sys.argv) != 4:
        sys.exit("Usage: python3 programming_hw3.py <-pre | -post> <input> <output>")
    
    # 2. Read the input file
    inFile = open(sys.argv[2], 'r')
    input_list = list(inFile.read().splitlines())
    inFile.close()
    # print(input_list)

    # 3. Solve
    if sys.argv[1] == '-pre':
        answer_list = [ preorder_check(s) for s in input_list ]
    elif sys.argv[1] == '-post':
        answer_list = [ postorder_check(s) for s in input_list ] 
    # print(answer_list)

    # 4. Output answers
    outFile = open(sys.argv[3], 'w')
    for ans in answer_list:
        outFile.write('{}\n'.format(ans))
    outFile.close()
