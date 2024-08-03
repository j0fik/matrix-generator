import random
n = int(input("Enter dimension of matrix: 3 for 3x3, 4 for 4x4: "))
d = int(input("Entrer number of generated matrices: "))
#generates matrix - input is dimension
def generate_matrix(a):
    matrix = []
    for i in range(a):
        row = []
        for j in range(a):
            x = random.randint(-5, 7)
            row.append(x)
        matrix.append(row)
    return matrix

#write the matrix by rows
def show_matrix(a):
    for rows in a:
        print(rows)

#Decide whether is matrix regular/singular and returns a determinant - input is 3x3 matrix
def determinant(b):
    global n
    D = b[0][0]*b[1][1]*b[2][2] + b[1][0]*b[2][1]*b[0][2] + b[2][0]*b[0][1]*b[1][2] - b[2][0]*b[1][1]*b[0][2] - b[0][0]*b[2][1]*b[1][2] - b[1][0]*b[0][1]*b[2][2]
    if n == 3:
        if D != 0:
            print(f"Matrix is regular, its determinant is |A|={D}")
        else:
            print(f"Matrix is singular, its determinant is |A|={D}")
    return D

#returns a minor - input is 4x4 matrix, indexes i and j
def minor(a, i, j):
    minormtx = []
    for x in range(len(a)):
        if x != i:
            row = []
            for y in range(len(a[x])):
                if y != j:
                    row.append(a[x][y])
            if row:
                minormtx.append(row)
    return minormtx

#Decide whether is matrix regular/singular and returns a determinant - input is 4x4 matrix
def det_four(a):
    i = 0
    det = 0
    minr =0
    for j in range(4):
        minr = minor(a, i, j)
        m = determinant(minr)
        c_ij = (-1)**(i+j)
        det += a[i][j]*m*c_ij
    if det != 0:
        print(f"Matrix is regular, its determinant is |A|={det}")
    else:
        print(f"MMatrix is singular, its determinant is |A|={det}")
    return det

#write code for LaTeX matrix - input is 3x3 matrix
def latex_matrix(a):
    print(r"\[")
    print(r"\begin{bmatrix}")
    print(f"{a[0][0]} & {a[0][1]} & {a[0][2]} \\\\")
    print(f"{a[1][0]} & {a[1][1]} & {a[1][2]} \\\\")
    print(f"{a[2][0]} & {a[2][1]} & {a[2][2]}")
    print(r"\end{bmatrix}")
    print(r"\]")

#write code for LaTeX matrix - input is 4x4 matrix
def latex_four(a):
    print(r"\[")
    print(r"\begin{bmatrix}")
    print(f"{a[0][0]} & {a[0][1]} & {a[0][2]} & {a[0][3]} \\\\")
    print(f"{a[1][0]} & {a[1][1]} & {a[1][2]} & {a[1][3]} \\\\")
    print(f"{a[2][0]} & {a[2][1]} & {a[2][2]} & {a[2][3]} \\\\")
    print(f"{a[3][0]} & {a[3][1]} & {a[3][2]} & {a[3][3]}")
    print(r"\end{bmatrix}")
    print(r"\]")

for i in range(d):
    a = generate_matrix(n)
    show_matrix(a)

    if n == 3:
        determinant(a)
        latex_matrix(a)
    else:
        det_four(a)
        latex_four(a)
