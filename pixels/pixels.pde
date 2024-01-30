//
// pixels.pde
//


PImage gadget;
PImage tux;

String cat = "Gadget";

boolean red = false;
boolean green = false;
boolean blue = false;
boolean mirror = false;
boolean grey = false;


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


void clearFilters()
{
    red = false;
    green = false;
    blue = false;
    mirror = false;
    grey = false;
}


void draw()
{
    background(0);

    PImage current = cat.equals("Gadget") ? gadget : tux;
    applyFilters(current);
    image(current, 0, 0);
}


int index(int i, int j)
{
    return i*width + j;    
}


void applyRedFilter(int[] pixels)
{
    for (int i=0; i<pixels.length; i++)
        pixels[i] &= 0xffff0000;
}


void applyGreenFilter(int[] pixels)
{
    for (int i=0; i<pixels.length; i++)
        pixels[i] &= 0xff00ff00;
}


void applyBlueFilter(int[] pixels)
{
    for (int i=0; i<pixels.length; i++)
        pixels[i] &= 0xff0000ff;
}


void applyMirrorFilter(int[] pixels)
{
    for (int i=0; i<height; i++)
    for (int j=0; j<width/2; j++)
        pixels[index(i,width-j-1)] = pixels[index(i,j)]; 
}


void applyGreyFilter(int[] pixels)
{
    for (int i=0; i<pixels.length; i++)
    {
        int r = (pixels[i] & 0x00ff0000)>>16;
        int g = (pixels[i] & 0x0000ff00)>>8;
        int b = pixels[i] & 0x000000ff;
        int grey = (r + g + b)/3;
        pixels[i] = 0xff000000 | grey<<16 | grey<<8 | grey;
    }
}


void applyFilters(PImage img)
{
    img.loadPixels();

    if (red) applyRedFilter(img.pixels);
    if (green) applyGreenFilter(img.pixels);
    if (blue) applyBlueFilter(img.pixels);
    if (mirror) applyMirrorFilter(img.pixels);
    if (grey) applyGreyFilter(img.pixels);

    img.updatePixels();
}


void keyPressed()
{

    if (key == ' ')
        cat = cat.equals("Gadget") ? "Tux" : "Gadget";

    else if (key == 'r') red = !red;
    else if (key == 'g') green = !green;
    else if (key == 'b') blue = !blue;
    else if (key == 'm') mirror = !mirror;
    else if (key == 'c') grey = !grey;
    else if (keyCode == ENTER) clearFilters();

    initializeImages();
}


