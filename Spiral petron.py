import turtle
import random
turtle.bgcolor("black")
seurat=turtle.Turtle()

width=5
height=7
seurat.penup()
List_color=["white","yellow","brown","red","blue","green","orange","pink","violet","gray"]
dot_distance=25
seurat.setpos(-250,250)

def spiral(m,n):
    k=0 
    l=0
    f=0
    seurat.color("White")
    '''
    k= index of starting row
    l= index of starting coloumn
    '''
    while(k<m and l<n):
        if(f==1):
            seurat.right(90)
            seurat.color(random.choice(List_color))
        # Printing the first row from remaining rows.
        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[k][i],end=" ")
        k+=1
        f=1
        seurat.color(random.choice(List_color))
        seurat.right(90)
        # Printing the last line from remaining colomn
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[i][n-1], end=" ")
        n=n-1
        seurat.color(random.choice(List_color))
        seurat.right(90)
        # printing the last row from remaining rows
        if(k<m):
            for i in range(n-1,l-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[m-1][i],end=" ")
            m-=1
        seurat.color(random.choice(List_color))
        seurat.right(90)    
        # Printing the first coloum from remaining coloum
        if(l<n):
            for i in range(m-1,k-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[i][l],end=" ")
            l+=1
spiral(20,20)
turtle.done()