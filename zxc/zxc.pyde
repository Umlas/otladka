b=0
def setup():
    size(900,900)
    background(1)
def draw():
    global b
    background(1)
    rect(500,500,80,30)
    textSize(200)
    text( b, 200,200)
def mouseClicked():
     global b
     global x
     global y
     if mouseX>500 and mouseX<580 and mouseY>500 and mouseY<580:
         b=b+1
   
    
