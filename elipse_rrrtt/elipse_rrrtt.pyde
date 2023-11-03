y=20
x=20
def setup():
    size(900,900)
def draw():
    global y,x
    background(144,234,33)
    ellipse(450,450,x,y)
    if x>600 and y>600:
        x=0
        y=0
    x=x+1
    y=y+1
