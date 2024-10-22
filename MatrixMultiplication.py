# Multiplies two matrices A and B to output C
# It's glorified numpy but not even glorified

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

    return(int(M),int(N[::-1]))

def Values(Rows,Cols,MatrixID):
    Matrix = [[0 for x in range(Cols)] for y in range(Rows)]

    for i in range(0,Rows,1):
        row = input("Enter Row"+MatrixID+str(i+1)+" separated by spaces: ")
        for j in range(0,Cols,1):
            Matrix[i][j] = str2num(row.split(" ")[j])

    return(Matrix)

def str2num(x):
    return(float(Fraction(x)))

def Multiplication(A, B, RowsC, ColsC, InnerDim):
    C = [[0 for x in range(ColsC)] for y in range(RowsC)]

    for i in range(RowsC):
        for j in range(ColsC):
            for l in range(InnerDim):
                C[i][j] += A[i][l]*B[l][j]
            C[i][j] = round(C[i][j],3)

    return(C)

def Printing(C):
    print("\nMatrix C:")
    for i in range(len(C)):
        print(str(C[i][:]))

def ValidateDimensions(X,Y):
    return("" if X==Y else exit("Inner dimensions do not match."))
    
print("\n")
Am, An = Dimensions("A")
Bn, Bo = Dimensions("B")
ValidateDimensions(An,Bn)
MxA, MxB = Values(Am,An," A "), Values(Bn,Bo," B ")
Printing(Multiplication(MxA,MxB,Am,Bo,An))