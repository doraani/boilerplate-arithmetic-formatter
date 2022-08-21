#arithmetic_arranger
def arithmetic_arranger(arithmetic_array,show_result=False):
    arranged_problems =''
    max_digits = 4
    max_problems = 5
    line = '-'
    list1 = []
    list2 = []
    list3 = []
    spaces = []
    if len(arithmetic_array)>max_problems:
        return "Error: Too many problems."
    for i in arithmetic_array:
        e = i.split(' ')
        #check for operator input errors
        if e[1] != '-' and e[1] != '+':
            return "Error: Operator must be '+' or '-'."
        if not (e[0]).isdigit() or not (e[2]).isdigit():
            return "Error: Numbers must only contain digits."
        if len(e[0])>max_digits or len(e[2])>max_digits: 
            return "Error: Numbers cannot be more than four digits."
        spaces.append(abs(len(e[0]) - len(e[2])))
        list1.append(e[0])
        list2.append(e[1])
        list3.append(e[2])
    #print first operand1
    len1 = len(list1)
    for i in range(0,len1):
        if len(list1[i])>len(list3[i]):
            arranged_problems+=' '*2+list1[i]
        else:
            arranged_problems+=' '*(spaces[i]+2)+list1[i]
        if i < len1-1:
            arranged_problems+=' '*4
    arranged_problems+='\n'
    #print operator and operand2
    for i in range(0,len(list3)):
        if len(list1[i])>len(list3[i]):
            arranged_problems+=list2[i]+' '*(spaces[i]+1)+list3[i]
        else:
            arranged_problems+=list2[i]+' '+list3[i]
        if i < len1-1:
            arranged_problems+=' '*4
    arranged_problems+='\n'
    #print line --- and result
    for i in range(0,len(list3)):
        res = eval(list1[i]+list2[i]+list3[i])
        line = '-'*(max(len(list1[i]),len(list3[i]))+2)
        arranged_problems+=line
        if i<len1-1: 
            arranged_problems+=' '*4
    if (show_result):
        arranged_problems+='\n'
        for i  in range(0,len(list1)):
            res = eval(list1[i]+list2[i]+list3[i])
            line_len = (max(len(list1[i]),len((list3[i])))+2) # +2 sign and space
            space = (line_len-len(str((res))))
            arranged_problems+=' '*space+str(res)
            if i<len1-1:
                arranged_problems+=' '*4
    
    return arranged_problems
