def setup():
  sizeRatio = 0.8
  x = int(1920 * sizeRatio)
  y = int(1080 * sizeRatio)
  size(1280, 900) 
  strokeWeight(2)
  strokeCap(SQUARE)
  colorMode(HSB, 360, 1, 1, 1)
 

def dtime(divideBy):
  return millis() / divideBy 

def draw():
  invertedMouseX = width-mouseX
  invertedMouseY = height-mouseY
  conv = 1/255
  time = millis()
  PI = 3.1415
  PI2 = PI*2
  fill(0,0,0, 0.1)
  rect(0,0,width, height)
  fill(0,0,1)
  stroke(0,0,1,1) 

  midX = width/2
  midY = height/2

  columns = 20
  rows = 20
  ms = millis()

  spacingX = (width/columns)
  spacingY = (width/rows)
  hexRatio = 1.155

  for x in range(columns):
    posX = spacingX * x
    ratioX = max(0.00001, spacingX * x) / width
    #text(ratioX, 50, 20 + 20*x)

    for y in range(rows):
      offsetX = (x % 2) * spacingX * 0.5
      posY = (spacingY * y + offsetX) * hexRatio

      distance = dist(posX, posY, midX, midY) * 0.001

      distanceGradientFromCenter = 1.0/distance*50


      distance = max(min(distance, 1), 0)
      size = sin(ms%PI2)
      size = (100.0 / width) * invertedMouseY
      size *= 1-distance
      
      rotation = (PI2 * 1 / height) * invertedMouseX
      
      rotation += dtime(2000)
      
      stroke(distanceGradientFromCenter, 1, 1)

      Hexagon(posX, posY, size, rotation)
   
  

def Hexagon(x, y, size, rotation):
  for i in range(6):
    curr = i
    next = (i+1) % 6
    x1 = (x) + sin(((PI*2)/6)*curr + rotation) * size
    y1 = (y) + cos(((PI*2)/6)*curr + rotation) * size     
    x2 = (x) + sin(((PI*2)/6)*next + rotation) * size
    y2 = (y) + cos(((PI*2)/6)*next + rotation) * size
    if(i%2==0):
      line(x1, y1, x, y)
    line(x1, y1, x2, y2)
   