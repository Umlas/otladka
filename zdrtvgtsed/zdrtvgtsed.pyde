x=20
direX=1
def setup():
    size(900,900)
def draw():
    global direX
    global x
    
    background(1)
    strokeWeight(23)
    stroke(32,0,11)
    point(random(900),random(900))
    textSize(35)
    fill(90,234,34)
    text("kokoko",350,x)
    x=x+direX
    if x>900:
       direX=-1
    if x<1:
        direX=1
