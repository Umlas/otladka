x=10
y=10
c=10
v=10
b=10
def setup():
    size(900,900)
    background(1)
def draw():
    global x
    global y
    global c
    global v 
    global b
    stroke(c,v,b)
    fill(c,v,b,)
    fill(c,v,b,)
    if mousePressed:
        ellipse(mouseX,mouseY,x,y)
    if keyPressed:
        if key == 'A' or key == 'a':
            x=x-1
            y=y-1
        if key== 'd' or key== 'D':
            x=x+1
            y=y+1
        if key== 'w' or key== 'W':   
            c=c+1
        if key== 's' or key== 'S': 
            v=v+1
        if key=='z' or key== 'Z':
            background(1)    
        if key=='x':
            b=b+1
        if key=='q':
            c=0
            v=0
            b=0
            
               
                  
                        
            
            
            
            
            
