############################################
#   107-1 Data Structure and Programming
#   Programming Assignment #5
#   Instructor: Pei-Yuan Wu
############################################

import sys

# **********************************
# *  TODO                          *
# **********************************
def solution(input_K, input_integer_set):

    quick_sort(input_integer_set, 0, len(input_integer_set)-1)

    min_diff = input_integer_set[0+input_K-1] - input_integer_set[0]
    for i in range(len(input_integer_set)-input_K):
        new_diff = input_integer_set[i+input_K-1] - input_integer_set[i]
        if new_diff < min_diff:
            min_diff = new_diff

    return min_diff

def quick_sort(input_list, first, last):

    if first < last:
        splitpoint = partition(input_list,first,last)
        quick_sort(input_list,first,splitpoint-1)
        quick_sort(input_list,splitpoint+1,last)

def partition(input_list, first, last):
    pivot = input_list[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and input_list[leftmark] <= pivot:
            leftmark = leftmark + 1

        while input_list[rightmark] >= pivot and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = input_list[leftmark]
            input_list[leftmark] = input_list[rightmark]
            input_list[rightmark] = temp

    temp = input_list[first]
    input_list[first] = input_list[rightmark]
    input_list[rightmark] = temp

    return rightmark


# **********************************
# *  Do NOT modify the code below  *
# **********************************
if __name__ == '__main__':
    # 1. Check the command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 programming_hw5.py <input> <output>")
    
    # 2. Read the input file
    inFile = open(sys.argv[1], 'r')
    input_list = list(inFile.read().splitlines())
    inFile.close()

    # 3. Solve
    input_k = int(input_list[0])
    input_set = input_list[1].split(',')
    input_set = [ int(s) for s in input_set ]
    answer = solution(input_k, input_set) 

    # 4. Output answers
    outFile = open(sys.argv[2], 'w')
    outFile.write(str(answer))
    outFile.close()
