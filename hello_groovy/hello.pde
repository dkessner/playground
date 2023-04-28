



class Ball
{
  float x = 200;
  float y = 200;
  float vx = random(-5, 5);
  float vy = random(-5, 5);

  float r = random(10, 40);;
  int c = color(random(255), random(255), random(255));

  void display()
  {
      fill(c);
      ellipse(x, y, 2*r, 2*r);

      x += vx;
      y += vy;

      if (x<r || x>width-r)
        vx *= -1;

      if (y<r || y>height-r)
        vy *= -1;
  }
}


ArrayList<Ball> balls;


void setup()
{
    size(400, 400);

    balls = new ArrayList<Ball>();
}


void draw()
{
    background(0);

    for (Ball b : balls)
      b.display();
}


void keyPressed()
{
    balls.add(new Ball());
}


