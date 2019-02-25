from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = [[],[],[],[]]
#m4 = [[1,3,4,2],[2,2,3,1],[3,1,2,3],[1,1,1,1]]
#m2 = [[1,4],[2,5],[3,6],[1,1]]
m3 = [[1,4,7,10],[2,5,8,11],[3,6,9,12],[1,1,1,1]]

#matrix_mult(m4,m2)
#print_matrix(m2)
print("Testing add_edge. Adding (1,2,3), (4,5,6) m2 = ")
add_edge(matrix,1,2,3,4,5,6)
print_matrix(matrix)
print("Testing ident. m1")
m1 = ident(m3)
print_matrix(m1)
print("Testing Matrix mult. m1 * m2")
matrix_mult(m1,matrix)
print_matrix(matrix)
for n in range(60):
    m = [[],[],[],[]]
    for x in range(0,500,10):
        add_edge(m,250,250,0,x,x%10+10,0)
    draw_lines(m,screen,[0,0,2 * n])
for n in range(60):
    m = [[],[],[],[]]
    for x in range(0,500,10):
        add_edge(m,250,250,0,x,x%10+100,0)
    draw_lines(m,screen,[0,2*n,0])
for n in range(60):
    m = [[],[],[],[]]
    for x in range(0,500,10):
        add_edge(m,250,250,0,x,x%10+200,0)
    draw_lines(m,screen,[2*n,0,0])
for n in range(60):
    m = [[],[],[],[]]
    for x in range(0,500,10):
        add_edge(m,250,250,0,x,x%10+300,0)
    draw_lines(m,screen,[0,0,2 * n])
for n in range(60):
    m = [[],[],[],[]]
    for x in range(0,500,10):
        add_edge(m,250,250,0,x,x%10+400,0)
    draw_lines(m,screen,[0,2*n,0])
for n in range(60):
    m = [[],[],[],[]]
    for x in range(0,500,10):
        add_edge(m,250,250,0,x,x%10+500,0)
    draw_lines(m,screen,[2*n,0,0])
display(screen)
