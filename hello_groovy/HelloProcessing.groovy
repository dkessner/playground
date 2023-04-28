import processing.core.*;


public class Hello extends PApplet
{
    public void settings()
    {
        size(400, 400);
    }

    public void setup()
    {
        
    }

    public void draw()
    {
        background(0);
        ellipse(200, 200, 100, 50);
    }

    public static void main(String[] args)
    {
        PApplet.main("Hello");
    }
}
