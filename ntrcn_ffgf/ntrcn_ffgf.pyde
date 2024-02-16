j=""
def setup():
    size(900,900)
def draw():
    global j
    frameRate(10)
    textSize(20)
    fill(0)
    if mousePressed == True:
        background(250)
    if keyPressed: 
        
        if key=="g" or key=="G":
            j=j+"g"
        text(j,200,200)
        if key=="h"or key=="H":
            j=j+"h"
        text(j,200,200)
