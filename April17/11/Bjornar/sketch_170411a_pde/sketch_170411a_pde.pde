void setup(){
  size(1280, 900); 
  strokeWeight(2);
  strokeCap(SQUARE);
  colorMode(HSB, 360, 1, 1);

  fill(0,0,0,255);
  rect(0,0,width, height);

  DrawTitle();
}

float oldMouseX = mouseX;
float oldMouseY = mouseY;

FloatList mouseHistory;

ArrayList<WildStroke> strokes = new ArrayList<WildStroke>();

class WildStroke{

  PVector p1;
  PVector p2;

  int lifeTime;

  int currentIteration;

  color col;

  float dirX;
  float dirY;

  float range;
  float decay;

  WildStroke(PVector in_p1, PVector in_p2, int in_lifeTime, color in_col, float in_dirX, float in_dirY, float in_range, float in_decay){
    p1 = in_p1;
    p2 = in_p2;

    lifeTime = in_lifeTime;
    currentIteration = 0;

    // use vecotr math plz
    dirX = in_dirX;
    dirY = in_dirY;

    range = in_range;
    decay = in_decay;

    strokes.add(this);
  }

  WildStroke(){
    p1 = new PVector(0,0);
    p2 = new PVector(0,0);

    lifeTime = 1;
    currentIteration = 0;

    dirX = 0;
    dirY = 0;

    range = 0;

    strokes.add(this);
  }

  void Iterate(){
    float h = hue(col);
    float s = saturation(col);
    float b = brightness(col);

    float i = max(this.currentIteration, 1);
    float ii = this.lifeTime - i;
    h = h ;
    s = s;// - 0.01;
    b = b;// - 0.01;

    this.col = color(h,s,b);

    stroke(this.col);
    line(this.p1.x, this.p1.y, this.p2.x, this.p2.y);
    p2 = p1.copy();
    this.range *= this.decay;
    p1.x = p1.x + random(0, this.range) * this.dirX * 1/width  * 5;
    p1.y = p1.y + random(0, this.range) * this.dirY * 1/height * 5;
    currentIteration += 1;
  }

  boolean NeedsToDie(){
    return currentIteration > lifeTime;
  }
}

float R(float range){
  return random(-range, range);
}

float R(float rangeMin, float rangeMax){
  return random(rangeMin, rangeMax);
}

boolean showDebug = false;

void HandleInput(){
  if(keyPressed){
    if(key == 'd'){
      showDebug = !showDebug;
    }
    if(key == 's'){
      saveFrame("######.png");
    }
  }
}

void draw()
{
  HandleInput();

  ArrayList<Object> Debugs = new ArrayList<Object>();

  PVector delta = new PVector(mouseX - oldMouseX, mouseY - oldMouseY);

  float mDeltaAvg = (abs(delta.x) + abs(delta.y)) / 2;

  Debugs.add(delta.mag());

  float invertedMouseX = width-mouseX;
  float invertedMouseY = height-mouseY;
  float conv = 1/255;

  float time = millis();
  float sec = time / 1000;


  float PI = 3.1415;
  float PI2 = PI*2;
  stroke(0,0,0,0);

  // Fill background
  fill(0,0,0,20);
  //rect(0,0,width, height);

  fill(0,0,0);

  float midX = width/2;
  float midY = height/2;

  int columns = 20;
  int rows = 20;
  float ms = millis();

  float spacingX = (width/columns);
  float spacingY = (width/rows);
  float hexRatio = 1.155;
  
  float jitterX = random(-20.0, 20.0);
  float jitterY = random(-20.0, 20.0);

  stroke(0, 0, 1);

  if(delta.mag() > 1 && mousePressed){

    float hue = hueStart;
    hue = R(hue, hue+60);
    hue = hue % 360;

    float brightness = 1;

    for (int i = 0; i < 50; ++i) {
      WildStroke stroke = new WildStroke();
      stroke.p1 = new PVector(mouseX + R(20), mouseY + R(20));
      stroke.p2 = stroke.p1.copy();
      stroke.lifeTime = (int)mDeltaAvg;
      stroke.col = color( hue + i, R(0.5, 0.8), R(0.7, 0.95));
      stroke.dirX = delta.x;
      stroke.dirY = delta.y;
      stroke.range = (int)mDeltaAvg;
      stroke.decay = 0.95;
    }
}

  for (WildStroke s : strokes) {
    s.Iterate();
  }

  for (int i = strokes.size()-1; i >= 0; --i) {
    if(strokes.get(i).NeedsToDie()){
      strokes.remove(i);
    }
  }

  oldMouseY = lerp(oldMouseY, mouseY, 0.1);
  oldMouseX = lerp(oldMouseX, mouseX, 0.1);

  Debugs.add("What");

  if(showDebug){
    DrawDebug(Debugs);
  }
}

float hueStart = 0;

void mousePressed(){
  hueStart = R(0, 360);
}

void StrokeSplash(float x, float y){
  // move drawing in here and make stroke averaging code...
}

void DrawTitle(){
  fill(0,0,1);
  text("Click and drag to do the thing", 10, height - 30);
}
void DrawDebug(Object... args){

  if(args.length == 0)
    return;
  float xPos = 10;
  float yPos = 20;
  float spacing = 20;
  float i = 0;

  // draw rect
  fill(0,0,1);
  stroke(0,0,0,0);
  rect(0,0, 200, (args.length + 1) * spacing);

  // text color
  fill(0,0,1);

  for (Object arg : args) {
    text(arg.toString(), xPos, yPos + spacing * i);
    i++;
  }

}