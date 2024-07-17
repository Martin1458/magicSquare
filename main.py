from validation import validate_square

n = 3
square_array = [[40 for i in range(n)] for j in range(n)]
square_array = [[40, 40, 40], [40, 40, 30], [40, 40, 40]]

def print_square(square):
    for i in range(n):
        for j in range(n):
            print(square[i][j], end=' ')
        print()       

print_square(square_array)

validate_square(square_array)
