# Determines the determinant of any n by n matrix A.
# Uses the Laplace Expansion formula along the first row (even if inefficient)
# May later add some functionality to expand along a column/row with most 0's but whatever

from fractions import Fraction

def Dimensions(Matrix):
    dims = str(input("Enter dimensions of "+Matrix+": "))
    M, N = "", ""

    for i in range(len(dims)):
        if dims[i].isnumeric():
            M += str(dims[i])
        else: break

    for i in reversed(range(len(dims))):
        if dims[i].isnumeric():
            N += str(dims[i])
        else: break

    return(int(M),int(N[::-1]) if M == N else exit("Dimensions must match."))

def Values(Rows,Cols):
    Matrix = [[0 for x in range(Cols)] for y in range(Rows)]

    for i in range(0,Rows,1):
        row = input("Enter Row "+str(i+1)+" separated by spaces: ")
        if len(row.split(" ")) > Cols:
            exit("Too many arguments entered")
        for j in range(0,Cols,1):
            Matrix[i][j] = str2num(row.split(" ")[j])

    return(Matrix)

def str2num(x):
    return(float(Fraction(x)))

def horzcat(Left,Right):
    # Horizontally concatenates two matrices (L, R) of the same number of rows
    rows = len(Left)
    cols = len(Left[0]) + len(Right[0]) 
    S = [[0 for x in range(cols)] for y in range(rows)]

    for i in range(rows):
        for j in range(0,len(Left[0])):
            S[i][j] = Left[i][j]

    for i in range(rows):
        for j in range(len(Left[0]), len(Right[0])+len(Left[0])):
            S[i][j] = Right[i][j-len(Left[0])]

    return(S)

def SubMatrix(A, StartR, EndR, StartC, EndC):
    # Extracts submatrix A[StartR:EndR][StartC:EndC] and returns it as S
    S = [[0 for x in range(EndC-StartC+1)] for y in range(EndR-StartR+1)]
    for i in range(0,EndR-StartR+1):
        for j in range(0,EndC-StartC+1):
            S[i][j] = A[i+StartR][j+StartC]
    return(S)

def Determinant(Matrix, Rows, Cols, det=0):
    if Rows == 2 or Cols == 2:
        #2x2 matrix case - no need for Laplace expansion
        return(Matrix[0][0]*Matrix[1][1] - Matrix[0][1]*Matrix[1][0])
    else:
        #Otherwise, employ the most basic algorithm to just expand along the first row
        for n in range(0,Cols):
            if n == 0:
                #Case 1: n = 0 (first column) - get the det of Row 1:x and Col 1:x
                LesserMatrix = SubMatrix(Matrix, 1,Rows-1, 1,Cols-1)
            elif n == Cols-1:
                #Case 2: n = Cols-1 (rightmost column) - get the det of Row 1:x and Col 0:Cols-2
                LesserMatrix = SubMatrix(Matrix, 1,Rows-1, 0,Cols-2)
            elif n > 0 and n < Cols-1:
                #Case 3: n is a column in the middle of the matrix.
                #First grab the left half (Cols 0 : n-1) and ALL ROWS 1:Rows-1
                LeftHalf = SubMatrix(Matrix, 1,Rows-1, 0,n-1)
                #Repeat for the right half (n+1 : Cols-1) and ALL ROWS 1:Rows-1
                RightHalf = SubMatrix(Matrix, 1,Rows-1, n+1,Cols-1)
                #Now use the horzcat function (name lazily stolen from matlab) to combine into one square matrix
                LesserMatrix = horzcat(LeftHalf,RightHalf)
            else:
                exit("unexpected situation")

            #Last, for each iteration, add to the current determinant per the Laplace Expansion summation formula
            det += Matrix[0][n] * (-1)**(2+n) * Determinant(LesserMatrix,Rows-1,Cols-1,0)        
        return(det)


Rows, Cols = Dimensions("A")
det = Determinant(Values(Rows,Cols), Rows, Cols)
print("\nDeterminant of A is: "+str(det))