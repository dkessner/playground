//
// clock.pde
//

PImage clock;

void setup()
{
    size(800, 600, P3D);
    clock = loadImage("clock2.png");
}

void draw()
{
    background(0);

    textureMode(NORMAL); 
    beginShape();
    texture(clock);
    vertex(40, 80, 20, 0, 0);
    vertex(720, 20, 40, 1, 0);
    vertex(780, 360, 60, 1, 1);
    vertex(mouseX, mouseY, 20, .5, 1);
    vertex(20, 380, 0, 1);
    endShape();


}


