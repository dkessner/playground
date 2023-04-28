import processing.core.*;

public class Ball
{
    public Ball(PApplet p)
    {
        this.p = p;
        radius = p.random(5, 100);
        position = new PVector(p.random(radius, p.width-radius),
                               p.random(radius, p.height-radius));
        velocity = PVector.random2D();
        velocity.setMag(p.random(2, 5));
        color = p.color(p.random(255), p.random(255), p.random(255));
    }

    public void display()
    {
        p.fill(color);
        p.ellipse(position.x, position.y, radius*2, radius*2);

        position.add(velocity);

        if (position.x<radius || position.x>p.width-radius)
            velocity.x *= -1;
        if (position.y<radius || position.y>p.height-radius)
            velocity.y *= -1;
    }

    public float radius() {return radius;}

    private PApplet p;
    private PVector position;
    private PVector velocity;
    private float radius;
    private int color;
}

