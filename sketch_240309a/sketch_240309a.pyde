x=10
y=10
def setup():
    size(900,900)
def draw():
    global x
    global y
    background(1)
    ellipse(400,400,x,y)
    if keyPressed:
        if key == 'A' or key == 'a':
            x=x+1
            y=y+1
        if key== 'd' or key== 'D':
            x=x-1
            y=y-1
