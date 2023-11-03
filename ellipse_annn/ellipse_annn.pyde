y=20
x=20
def setup():
    size(900,900)
def draw():
    global y,x
    background(123,23,43)
    ellipse(x,y,10,10)
    if x==900 and y==900:
        x=0
        y=0
    y=y+2
    x=x+2
    
    
