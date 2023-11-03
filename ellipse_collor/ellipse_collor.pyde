x=20
y=20
b=20
def setup():
    size(900,900)
def draw():
    global x,y,b
    fill(x,y,b)
    ellipse(450,450,400,400)
    if x>240 and y>240 and b>240:
        x=0
        y=0
        b=0
    x=x+1
    y=y+1
    b=b+1
    
