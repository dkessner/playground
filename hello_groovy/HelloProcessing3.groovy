import processing.core.*;
import java.util.*;


println "test"
def numbers = 1..10
numbers.each {println it}


public class HelloProcessing extends PApplet
{
    public void settings()
    {
        size(400, 400);
    }

    public void setup()
    {
        for (i in 1..20)
            balls add new Ball(this)
    }

    public void draw()
    {
        background(0);

        noStroke();
        balls.each {it.display()}

        stroke(255);
        /*
        // Java stream
        balls.stream()
             .filter(b -> b.radius() < 50)
             .forEach(b -> b.display());
        */

        balls.findAll {b -> b.radius() < 50}
            .each {b -> b.display()}
    }

    def balls = [];
}

PApplet.main("HelloProcessing");

