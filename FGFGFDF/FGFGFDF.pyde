x=20
direX=1
def setup():
    size(900,900)
def draw():
    global direX
    global x
    background(1)
    textSize(35)
    fill(90,234,34)
    text("2024",400,x)
    fill(255,255,255)
    ellipse(150,800,200,200)
    ellipse(150,650,150,150)
    ellipse(150,550,100,100)
    stroke(211,120,12)
    strokeWeight(10)
    line(700,900,700,800)
    strokeWeight(0)
    fill(90,234,34)
    triangle(600,800,800,800,700,700)
    triangle(650,700,750,700,700,650)
    triangle(700,650,700,650,700,600)
    triangle(500,350,600,350,500,200)
    x=x+direX
    if x>900:
       direX=-1
    if x<1:
        direX=1
        
