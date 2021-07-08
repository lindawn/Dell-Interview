input = [1,9,0,4,3,0,7,0]

def Solution3(input):
    zeroPointer = len(input)-1
    
    for i in range(len(input)-1):
        if input[i] == 0:
            input = input[0:i] + input[i+1:zeroPointer+1]
            input.append(0)
            # zeroPointer-=1
            print(input)
    return input
            
     

def Solution2(input):
    # zeroPointer = len(input-1)
    # endPointer = len(input-1)
    for i in range(len(input)):
        if input[i] == 0:
            input.pop(i)
            input.append(0)
    return input
            
            

def Solution(input):
    answer = []
    zeroCounter = 0
    for i in range(len(input)):
        if input[i] == 0:
            zeroCounter+=1
        else:
            answer.append(input[i])
    answer.extend([0]*zeroCounter)
    return answer


print(Solution(input))

