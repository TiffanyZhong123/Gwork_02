"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    xlen = len(matrix[0])
    for row in range (4):
        rowlist = []
        for n in matrix[row]:
            rowlist.append(str(n))
        print(' '.join(rowlist))
    print('\n')
    pass
#print_matrix([[1,2,3,4],[3,5,1,2],[3,1,4,6],[1,1,1,1]])

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    xlen = len(matrix[0])
    for x in range(xlen):
        for y in range(xlen):
            matrix[x][y] = 0
    for n in range(xlen):
        matrix[n][n] = 1
    return matrix
    pass
#m4 = ident([[1,2,3,4],[3,5,1,2],[3,1,4,6],[1,1,1,1]])
#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    #m1 is always 4 by 4
    #m2 is always 4 by n
    lenm2col = len(m2[0])
    m3 = [[],[],[],[]]
    for m1row in range(4):
        for m2col in range(lenm2col):
            sum = 0
            for m1m2 in range(4):
                sum += m1[m1row][m1m2] * m2[m1m2][m2col]
            m3[m1row].append(sum)
    #copy m3 into m2
    for row in range (4):
        for col in range(lenm2col):
            m2[row][col] = m3[row][col]
    return m2
    pass
#print_matrix(matrix_mult([[1,2,3,4],[3,5,1,2],[3,1,4,6],[1,1,1,1]],m4))




def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[c].append( 0 )
    return m
