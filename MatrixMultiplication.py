# Multiplies two matrices A and B to output C
# Does what numpy does I guess...

def Dimensions(Matrix):
    dims = input("Enter dimentions of "+Matrix+": ")
    M = int(dims[0:1])
    N = int(dims[len(dims)-1:len(dims)])
    return(M,N)
    # this function could be improved to accept inputs >1 digit (i.e. 10x10)

def Values(Rows,Cols,MatrixID):
    Matrix = [[0 for x in range(Cols)] for y in range(Rows)]

    for i in range(0,Rows,1):
        row = input("Enter Row"+MatrixID+str(i+1)+" separated by spaces: ")
        for j in range(0,Cols,1):
            Matrix[i][j] = row.split(" ")[j]
    return(Matrix)

def Multiplication(A, B, RowsC, ColsC, InnerDim):
    C = [[0 for x in range(ColsC)] for y in range(RowsC)]
    i = 0
    while i <= RowsC-1:
        j = 0
        while j <= ColsC-1:
            l = 0
            while l <= InnerDim-1:
                C[i][j] += float(A[i][l])*float(B[l][j])
                l+=1
            j+=1
        i+=1
    return(C)

    '''
    for i in (0, RowsC-1, 1):
        for j in (0, ColsC-1, 1):
            for l in (0, InnerDim-1, 1):
                C[i][j] += float(A[i][l])*float(B[l][j])
    # this doesn't work? i literally don't know how this is different from the while loop that DOES work...
    '''

def Printing(C):
   print("\nMatrix C:")
   i = 0
   while i <= len(C[0])-1: 
       print(str(C[i][0:len(C)])); i+=1
    # again i literally dont know why for i = (0, len(C[0])-1, 1) messes up but here we are...

Am, An = Dimensions("A")
Bn, Bo = Dimensions("B")

if An != Bn:
    print("Inner dimensions must match.")
    exit()

MxA = Values(Am,An," A ")
MxB = Values(Bn,Bo," B ")
MxC = Multiplication(MxA,MxB,Am,Bo,An)

Printing(MxC)
