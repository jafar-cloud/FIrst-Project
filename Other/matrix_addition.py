matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[1, 2, 3], [4, 5, 6]]

sum = [[0, 0, 0], [0, 0, 0]]


for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        sum[i][j] = matrix1[i][j] + matrix2[i][j]


print(sum)


class MyError(Exception):
    """My Own Error."""
    pass


# I Solved This Without Lists!
def is_balanced_expr(expr: str):
    if not isinstance(expr, str):
        raise MyError("Invalid expression.")

    if expr.count("(") == expr.count(")"):
        print(f"Expression '{expr}' is balanced.")
        return True
    else:
        print(f"Expression '{expr}' is not balanced.")
        return False
    

user_expr = input("Enter Expression: ")

is_balanced_expr(user_expr)
