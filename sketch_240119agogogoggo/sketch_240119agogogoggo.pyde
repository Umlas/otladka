x=10
dirX=1
def setup():
    size(900,900)
    
def draw():
    background(1)

    if mousePressed ==True:
            global x
            global dirX
            ellipse(x,400,50,50)
            x=x+dirX
            if x>800:
                dirX=-1
        
