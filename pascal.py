input = 6
          

def Solution(input):
    row1 = [1, 1] + [0]*(input-2)
    matrix = []
    matrix.append(row1)
    rowN = [1]
    rowN.extend([0]*(input-1))
    
    for i in range(input-1):
        matrix.append(rowN)
    # print(matrix)

    for m in range(1, input):
        for n in range(1, m+2):
            matrix[m][n] = matrix[m-1][n] + matrix[m-1][n-1]
            # print(m,n)
            print(matrix)
    return matrix


print(Solution(6))

