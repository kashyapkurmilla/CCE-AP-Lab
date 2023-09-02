def main():
    mat1 = []
    mat2 = []
    d1 = {}
    d2 = {}

    n1 = int(input('Enter order of matrix 1: '))
    mat1 = matrixInput(n1, mat1)
    d1 = NonZero(n1, mat1)

    n2 = int(input('Enter order of matrix 2: '))
    mat2 = matrixInput(n2, mat2)
    d2 = NonZero(n2, mat2)

    result_matrix = addMatrices(n1, d1, n2, d2)

    print("Matrix 1:")
    printMatrix(n1, d1)

    print("\nMatrix 2:")
    printMatrix(n2, d2)

    print("\nresult matrix in 2d:")
    printMatrix(n1, result_matrix)


def matrixInput(n, mat):
    for i in range(n):
        row = list(map(int, input(f"Enter values for row {i + 1}: ").split()))
        mat.append(row)
    return mat


def NonZero(n, mat):
    d = {}
    for i in range(n):
        for j in range(n):
            if mat[i][j] != 0:
                d[(i, j)] = mat[i][j]
    return d


def addMatrices(n1, d1, n2, d2):
    result_matrix = {}
    for i in range(n1):
        for j in range(n1):
            value1 = d1.get((i, j), 0)
            value2 = d2.get((i, j), 0)
            result_matrix[(i, j)] = value1 + value2
    return result_matrix


def printMatrix(n, mat_dict):
    for i in range(n):
        for j in range(n):
            value = mat_dict.get((i, j), 0)
            print(value, end=' ')
        print()


main()
