
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
        elif: len(sub_str) == 3:
            times == 1
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

print(solution("10010"))