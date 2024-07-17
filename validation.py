def validate_square(square):
    correct_sum = 120 #! Hardcoded for now
    square_valid = 0 # 0 = True
    if not validate_all_rows(square, correct_sum):
        square_valid += 1

    if not validate_all_columns(square, correct_sum):
        square_valid += 1

    if not validate_all_diagonals(square, correct_sum):
        square_valid += 1
        
    return square_valid == 0

def validate_row(square, row, correct_sum):
    row_sum = 0
    for i in range(len(square)):
        row_sum += square[row][i]
    
    if row_sum == correct_sum: 
        print("Row", row, "is correct")
        return True
    else: 
        print("Row", row, "is incorrect: ", row_sum, " != ", correct_sum)
        return False

def validate_all_rows(square, correct_sum):
    valid = 0 # 0 = True; so that it still prints all the results
    for row_num in range(len(square)):
        if not validate_row(square, row_num, correct_sum):
            valid += 1
    return valid == 0

def validate_column(square, column, correct_sum):
    column_sum = 0
    for i in range(len(square)):
        column_sum += square[i][column]
    
    if column_sum == correct_sum: 
        print("Column", column, "is correct")
        return True
    else: 
        print("Column", column, "is incorrect: ", column_sum, " != ", correct_sum)
        return False
    
def validate_all_columns(square, correct_sum):
    valid = 0 # 0 = True; so that it still prints all the results
    for column_num in range(len(square)):
        if not validate_column(square, column_num, correct_sum):
            valid += 1
    return valid == 0

def validate_downward_diagonal(square, correct_sum):
    diagonal_sum = 0
    for i in range(len(square)):
        diagonal_sum += square[i][i]
    
    if diagonal_sum == correct_sum: 
        print("Downward diagonal is correct")
        return True
    else: 
        print("Downward diagonal is incorrect: ", diagonal_sum, " != ", correct_sum)
        return False

def validate_upward_diagonal(square, correct_sum):
    diagonal_sum = 0
    for i in range(len(square)):
        diagonal_sum += square[i][len(square) - 1 - i]
    
    if diagonal_sum == correct_sum: 
        print("Upward diagonal is correct")
        return True
    else: 
        print("Upward diagonal is incorrect: ", diagonal_sum, " != ", correct_sum)
        return False

def validate_all_diagonals(square, correct_sum):
    valid = 0 # 0 = True; so that it still prints all the results
    if not validate_downward_diagonal(square, correct_sum):
        valid += 1
    if not validate_upward_diagonal(square, correct_sum):
        valid += 1
    return valid == 0