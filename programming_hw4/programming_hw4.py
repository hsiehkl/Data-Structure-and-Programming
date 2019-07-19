###########################################
#   107-1 Data Structure and Programming
#   Programming Assignment #4
#   Instructor: Pei-Yuan Wu
############################################

import sys

# **********************************
# *  TODO                          *
# **********************************
'''
You need to complete this class MinBinaryHeap()
Feel free to add more functions in this class.
'''
class MinBinaryHeap():
    def __init__(self):
        self.heap = [0] # with a dummy node
        self.heapSize = 0

    def insert(self, item):
        self.heap.append(item)
        self.heapSize = self.heapSize + 1
        self.perlocateUp(self.heapSize)

    def deleteMin(self):
        min = self.heap[1]
        self.heap[1] = self.heap[self.heapSize]
        self.heapSize = self.heapSize - 1
        self.heap.pop()
        self.perlocateDown(1)
        return min

    def findMin(self):
        return self.heap[1]

    def size(self):
        return self.heapSize
    
    def string(self):
        # Convert self.heap into a string
        return list2String(self.heap[1:])

    def perlocateUp(self, i):
        while (i // 2) > 0:
            if self.heap[i] < self.heap[(i // 2)]:
                tmp = self.heap[(i // 2)]
                self.heap[(i // 2)] = self.heap[i]
                self.heap[i] = tmp
            i = (i // 2)
    
    def perlocateDown(self, i):
        while (i * 2) <= self.heapSize:
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp
            i = mc

    def minChild(self, i):
        if (i * 2) + 1 > self.heapSize:
            return i * 2
        else:
            if self.heap[(i*2)] < self.heap[(i*2+1)]:
                return i * 2
            else:
                return (i * 2) + 1

def list2String(l):
    formatted_list = ['{}' for item in l ] 
    s = ','.join(formatted_list)
    return s.format(*l)

if __name__ == '__main__':
    # 1. Check the command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 programming_hw4.py <input> <output>")
    
    # 2. Read the input file
    inFile = open(sys.argv[1], 'r')
    input_line_list = list(inFile.read().splitlines())
    input_cmd_list = [ line.split(' ') for line in input_line_list ]
    inFile.close()

    # 3. Solve
    minPQ = MinBinaryHeap()
    findMin_list = []
    for cmd in input_cmd_list:
        if cmd[0] == 'insert':
            # print('insert {}'.format(cmd[1]))
            minPQ.insert(int(cmd[1]))
        elif cmd[0] == 'deleteMin':
            # print('deleteMin')
            if minPQ.size() > 0:
                minPQ.deleteMin()
        elif cmd[0] == 'findMin':
            # print('findMin')
            if minPQ.size() > 0:
                findMin_list.append(minPQ.findMin())
            else:
                findMin_list.append('-')
        else: # Unknown command
            assert False
        # print(minPQ.string())
    
    # 4. Output answers
    outFile = open(sys.argv[2], 'w')
    # 4.1 Output FindMin string
    outFile.write('{}\n'.format(list2String(findMin_list)))
    # 4.2 Output minPQ string
    outFile.write('{}'.format(minPQ.string()))
    outFile.close()
