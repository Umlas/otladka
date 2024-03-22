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
dirC=1
def setup():
    size(900,900)
def draw():
    global x
    global dirX
    global c
    global y
    global dirC
    background(32,124,144) 
    ellipse(c,y,50,50)
    rect(x,850,100,30)
    if c >899:
        c-1
    if dirC <1:
        dirC+1
    if keyPressed ==True:
        if key=='d':
            x=x+10
        if key=='a':
            x=x-10
