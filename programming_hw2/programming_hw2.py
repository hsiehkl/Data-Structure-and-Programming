############################################
#   107-1 Data Structure and Programming
#   Programming Assignment #2
#   Instructor: Pei-Yuan Wu
############################################

import sys
#sys.argv.append("input.txt")
#sys.argv.append("output.txt")

# **********************************
# *  TODO                          *
# **********************************
def solution(input_string):
    
    my_list = []
    
    cut_list = [1, 2, 3]

    for i in range(len(input_string)):
        
        times = 0
        digit = i + 1
        sub_str = input_string[:digit]
        
        if len(sub_str) == 1:
            times = 1
            
        elif len(sub_str) == 2:
            if int(sub_str[0]) == 0:
                times = 1
            else:
                times = 2
        else:
            
            for j in (l for l in cut_list if l <= len(sub_str)):
                
                sb2 = sub_str[-j:]
                
                if len(sb2) == 1:
                    times = my_list[-1]
                elif len(sb2) == 2 and int(sb2[0]) != 0:
                    times += my_list[-2]
                elif len(sb2) == 3 and int(sb2) == 100:
                    times += my_list[-3]
        my_list.append(times)
    return my_list[-1]

# **********************************
# *  Do NOT modify the code below  *
# **********************************
if __name__ == '__main__':
    # 1. Check the command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 programming_hw2.py <input> <output>")
    
    # 2. Read the input file
    inFile = open(sys.argv[1], 'r')
    input_list = list(inFile.read().splitlines())
    inFile.close()
    # print(input_list)

    # 3. Solve
    answer_list = [ solution(s) for s in input_list ]
    # print(answer_list)

    # 4. Output answers
    outFile = open(sys.argv[2], 'w')
    for ans in answer_list:
        outFile.write('{}\n'.format(ans))
    outFile.close()
