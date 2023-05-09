
import peasy.*;

PeasyCam cam;

TexturedShape shape;


class TexturedShape
{
    public TexturedShape()
    {
        ul = new PVector(-15, -15, 16);
        ur = new PVector(15, -15, 16);
        lr = new PVector(15, 15, 16);
        ll = new PVector(-15, 15, 16);
        img = loadImage("cats.jpg");
    }

    public void display()
    {
        noStroke();
        textureMode(NORMAL); 
        beginShape();
        texture(img);
        vertex(ul.x, ul.y, ul.z, 0, 0);
        vertex(ur.x, ur.y, ur.z, 1, 0);
        vertex(lr.x, lr.y, lr.z, 1, 1);
        vertex(ll.x, ll.y, ll.z, 0, 1);
        endShape();
    }

    private PVector ul, ur, lr, ll;
    private PImage img;
}


void setup()
{
    size(400, 400, P3D);

    cam = new PeasyCam(this, 100);
    cam.setMinimumDistance(50);
    cam.setMaximumDistance(500);

    shape = new TexturedShape();
}



void draw()
{
    background(0);

    fill(255,0,0);
    box(30);

    shape.display();

    //drawTexture();
}



void keyPressed()
{
    if (key == 'a')
      shape.ul.x--;
    else if (key == 'd')
      shape.ul.x++;
    else if (key == 'w')
      shape.ul.y--;
    else if (key == 's')
      shape.ul.y++;

}




/*
void drawTexture()
{
    noStroke();
    textureMode(NORMAL); 
    beginShape();
    texture(img);
    vertex(-15, -15, 16, 0, 0);
    vertex(15, -15, 16, 1, 0);
    vertex(15, 15, 16, 1, 1);
    vertex(-15, 15, 16, 0, 1);
    endShape();
}
*/


