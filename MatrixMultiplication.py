# Multiplies two matrices A and B to output C
# It's glorified numpy but not even glorified

#aware of some problems with small dimensions i.e. 1x2 x 2x2 fails at printing

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
            Matrix[i][j] = ValueCleaning(row.split(" ")[j])

    return(Matrix)


def ValueCleaning(x):
    return(float(Fraction(x)))


def Multiplication(A, B, RowsC, ColsC, InnerDim):
    C = [[0 for x in range(ColsC)] for y in range(RowsC)]

    for i in range(RowsC):
        for j in range(ColsC):
            for l in range(InnerDim):
                C[i][j] += round(A[i][l]*B[l][j],3)

    return(C)


def Printing(C):
   print("\nMatrix C:")
   for i in range(len(C[0])):
       print(str(C[i][0:len(C)]))

Am, An = Dimensions("A")
Bn, Bo = Dimensions("B")

if An != Bn:
    print("Inner dimensions must match.")
    exit()

MxA = Values(Am,An," A ")
MxB = Values(Bn,Bo," B ")
MxC = Multiplication(MxA,MxB,Am,Bo,An)

Printing(MxC)