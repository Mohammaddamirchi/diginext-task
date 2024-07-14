def searchmatrix(matrix , target):
    print(matrix[0])
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // n][mid % n]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# مثال : 

matrix = [
    [1, 3, 5],
    [7, 8, 10], 
    [12, 15, 18]
]

target = 15

print(searchmatrix(matrix, target)) 

