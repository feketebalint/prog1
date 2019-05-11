def AHM(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i < j:
                if matrix[i][j] != 0:
                    return False
    return True
print(AHM([[4,0,0,0],[5,1,0,0],[4,5,6,0],[9,23,12,1]]))
