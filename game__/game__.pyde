def collideRectCircle(rx, ry, rw, rh, cx, cy, diameter):

  #2d

  # временные переменные для установки краёв для тестирования

  # rectmode — CORNER, ellipseMode — CENTER, то есть оба по-умолчанию

  testX = cx

  testY = cy


  # which edge is closest?

  if cx < rx:

    testX = rx       # Левый край

  elif cx > rx+rw:

    testX = rx+rw     # правый край


  if cy < ry:

    testY = ry       # верхний край

  elif cy > ry+rh:

    testY = ry+rh   # нижний край


  # получить расстояние от ближайших краев с помощью processing функции dist()

  distance = dist(cx,cy,testX,testY) 


  # если расстояние меньше радиуса, столкновение!

  if distance <= diameter/2:

    return True

  else:

    return False
j=50
h=50
g=255
dirX=10
x=10
c=10
y=10
dirC=4
dirY=8
v=20
b=20
r=20
t=20
Y=20
u=20
i=20
o=20
p=20
l=20
sf=0
pouse=False
def setup():
    size(900,900)

def draw():
    
    global g
    global r
    global t
    global Y
    global u
    global i
    global o
    global p
    global l
    global h
    global j
    global v
    global b
    global dirY
    global x
    global dirX
    global c
    global y
    global dirC
    global sf

    if collideRectCircle(432,465,20,20,c,y,50):
        v=0
        b=0
    if collideRectCircle(332,535,20,20,c,y,50):
        r=0
        t=0
    if collideRectCircle(782,665,20,20,c,y,50):
        Y=0
        u=0
    if collideRectCircle(212,225,20,20,c,y,50):
        i=0
        o=0
    if collideRectCircle(479,344,20,20,c,y,50):
        p=0
        l=0
    if collideRectCircle(x,850,150,30,c,y,50):
         if c >850:
            dirC=-2
         if c<1:
            dirC=2
         y=y+dirY
         if y >850:
            dirY=-6
         if y<1:
            dirY=6 
    
    rect(432,465,20,200)
    background(2) 
    rect(432,465,v,b)
    rect(332,535,r,t)
    rect(782,665,Y,u)
    rect(212,225,i,o)
    rect(479,344,p,l)
    ellipse(c,y,j,h)
    rect(x,850,150,30)
    c=c+dirC
    text(sf,80,25)
    if r==0:
        sf=1
    if Y==0:
        sf=4
    if i==0:
        sf=3
    if p==0:
        sf=4
    if v==0:
        sf=1
    if c >900:
       dirC=-4
    if c<1:
        dirC=4
    y=y+dirY
    if y<1:
        dirY=8
    if y >900:
        fill(g,0,0)
        textSize(60)
        text("game over",400,400)
        textAlign(CENTER,CENTER)
        

    if keyPressed ==True:
        if key=='d':
            x=x+10
        if key=='a':
            x=x-10
        if 1key=='e':
            exit()
    if i==0:вв
        fill(0,245,0)
        textSize(80)
        text("YOU WIN",400,400)
        textAlign(CENTER,CENTER)
        dirC=0
        dirY=0
        h=h=0
        j=j=1
