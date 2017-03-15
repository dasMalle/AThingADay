import oscP5.*;
import netP5.*;

float fCount = 0;
OscP5 oscP5;
NetAddress myRemoteLocation;

float gx, gy, gz;

void setup() {
    size(640,360,P3D);
    frameRate(60);
    
    background(0);
    lights();
    
    OscProperties properties = new OscProperties();
    properties.setListeningPort(6200);
    properties.setDatagramSize(99999999);

    oscP5 = new OscP5(this,properties);
}

void draw() {
    fCount += 1;
    
    background(0);
    lights();
    pushMatrix();
    translate(width/2, height/2, 0);
    rotateX(gx);
    rotateY(gy);
    rotateZ(gz);
    noStroke();
    fill(255);
    box(150);
    popMatrix();
}

void oscEvent(OscMessage theOscMessage) {
  /* print the address pattern and the typetag of the received OscMessage */
  String addr = theOscMessage.addrPattern();
  
  if ( addr.equals("/rigidBody") ) {
    Object[] args = theOscMessage.arguments();
    int index = 0;
    
    int id = (int)args[index++];
    String name = (String)args[index++];
    
    if ( name.equals("Cube") ) {
      float x = (float)args[index++];
      float y = (float)args[index++];
      float z = (float)args[index++];
      
      float qx = (float)args[index++];
      float qy = (float)args[index++];
      float qz = (float)args[index++];
      float qw = (float)args[index++];
      
      float[] rot = getRotationFromQuat( qx, qy, qz, qw );
      
      gx = rot[0];
      gy = rot[1];
      gz = rot[2];
      
      print( rot[0], rot[1], rot[2], "\n" );
    }
  }
}

float[] getRotationFromQuat( float x, float y, float z, float w)
{
    float[] rot = new float[3];
    
    rot[0] = atan2(-2.0 * (y * z - w * x), w * w - x * x - y * y + z * z);
    rot[1] = asin(2.0 * (x * z - w * y));
    rot[2] = atan2(-2.0 * (x * y - w * z), w * w + x * x - y * y - z * z);

    // rot[0] = degrees(rot[0]);
    // rot[1] = degrees(rot[1]);
    // rot[2] = degrees(rot[2]);

    return rot;
}