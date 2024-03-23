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
dirX=10
x=10
c=10
y=10
dirC=4
dirY=8
v=20
b=20
def setup():
    size(900,900)

def draw():
    global v
    global b
    global dirY
    global x
    global dirX
    global c
    global y
    global dirC

    if collideRectCircle(432,465,20,20,c,y,50):
        v=0
        b=0
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
    background(32,124,144) 
    rect(432,465,v,b)
    ellipse(c,y,50,50)
    rect(x,850,150,30)
    c=c+dirC
    if c >900:
       dirC=-4
    if c<1:
        dirC=4
    y=y+dirY
    if y<1:
        dirY=8
    if y >900:
        fill(255,0,0)
        textSize(60)
        text("game over",400,400)
        textAlign(CENTER,CENTER)
        

    if keyPressed ==True:
        if key=='d':
            x=x+10
        if key=='a':
            x=x-10
        if key=='e':
            exit()
