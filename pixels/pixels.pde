//
// pixels.pde
//


PImage gadget;
PImage tux;

String cat = "Gadget";
boolean red = false;


void setup()
{
    size(800, 600);

    initializeImages();
}


void initializeImages()
{
    gadget = loadImage("gadget.jpg");
    tux = loadImage("tux.jpg");
}


void draw()
{
    background(0);

    PImage current = cat.equals("Gadget") ? gadget : tux;
    applyFilters(current);
    image(current, 0, 0);

    fill(255);
    textSize(30);
    text("red: " + red, 50, 50);
}



void applyRedFilter(int[] pixels)
{
    for (int i=0; i<pixels.length; i++)
        pixels[i] &= 0xffff0000;
}



void applyFilters(PImage img)
{
    img.loadPixels();

    if (red)
      applyRedFilter(img.pixels);

    img.updatePixels();
}



void keyPressed()
{

    if (key == ' ')
        cat = cat.equals("Gadget") ? "Tux" : "Gadget";

    else if (key == 'r')
      red = !red;

    initializeImages();
}



