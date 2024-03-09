x=10
y=10
def setup():
    size(900,900)
def draw():
    global x
    global y
    background(1)
    ellipse(x,y,50,50)
    if keyPressed:
        if key == 'A' or key == 'a':
            x=x-1
        if key== 'd' or key== 'D':
            x=x+1
        if key== 'w' or key== 'W':   
            y=y-1
        if key== 's' or key== 'S': 
            y=y+1    
            
            
            
            
            
            
            
