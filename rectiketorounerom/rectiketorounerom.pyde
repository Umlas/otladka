dirX=1
x=10
def setup():
    size(900,900)
def draw():
    global x,dirX
    background(32,124,144) 
    rect(200,200,x,x)
    x=x+dirX
    if x > 600:
        dirX=-1
    if x <1:
       dirX=1


    

    
