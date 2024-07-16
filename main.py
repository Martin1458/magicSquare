
n = 3
square_array = [[40 for i in range(n)] for j in range(n)]

def print_square(square):
    for i in range(n):
        for j in range(n):
            print(square[i][j], end=' ')
        print()       

print_square(square_array)

def validate_square(square):
    valid = 0 # 0 = True
    correct_sum = 120 #! Hardcoded for now
    for row_num in range(square):
        if not validate_row(square, row, correct_sum):
            valid += 1
    return valid == 0

def validate_row(square, row, correct_sum):
    row_sum = 0
    for i in range(n):
        row_sum += square[row][i]
    
    if row_sum == correct_sum: 
        print("Row", row, "is correct")
        return True
    else: 
        print("Row", row, "is incorrect: ", row_sum, "!= ", correct_sum)
        return False

validate_square(square_array)
