import processing.core.*;
import java.util.*;


public class HelloProcessing extends PApplet
{
    public void settings()
    {
        size(400, 400);
    }

    public void setup()
    {
        balls = new ArrayList<Ball>();
        for (int i=0; i<10; i++)
            balls.add(new Ball(this));
    }

    public void draw()
    {
        background(0);

        for (Ball b : balls)
            b.display();
    }

    ArrayList<Ball> balls;

    public static void main(String[] args)
    {
        PApplet.main("HelloProcessing");
    }
}

