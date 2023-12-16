x=20
direX=30
p=0
def setup():
    global p
    p=loadImage("moon.png")
    size(900,900)
def draw():
    global p
    global direX
    global x
    
    background(31,38,79)
    image(p,20,20,250,250)
    textSize(35)
    fill(255,255,255)
    text("2024",400,x)
    fill(255,255,255)
    ellipse(150,800,200,200)
    ellipse(150,650,150,150)
    ellipse(150,550,100,100)
    fill(1,1,1)
    ellipse(130,540,10,10)
    ellipse(170,540,10,10)
    fill(255,96,15)
    ellipse(150,570,15,15)
    stroke(211,120,12)
    strokeWeight(10)
    line(700,900,700,800)
    strokeWeight(0)
    fill(90,234,34)
    triangle(600,800,800,800,700,700)
    triangle(650,700,750,700,700,650)
    triangle(700,650,700,650,700,600)
    triangle(725,650,675,650,700,625)
    
    x=x+direX
    if x>900:
       direX=-1
    if x<1:
        direX=1
    dr()
def dr():
    frameRate(100)
    for i in range(50):
        frameRate(10)
        strokeWeight(random(15))
        stroke(250,250,250)
        point(random(900),random(900))
