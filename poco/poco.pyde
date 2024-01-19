img=0
x=300
def setup():
    size(900,900)
    img=loadImage("poco.jpg")
def draw():
    global img
    global x
    if mouseButton==RIGHT:
        
        image(img,40,40,x,x)
        x=x+1
        
        
