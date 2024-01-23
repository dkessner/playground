//
// clock.pde
//


import peasy.*;

PeasyCam cam;

PImage clock;

int rowCount = 100;
int columnCount = 100;
float gridSize = 400/rowCount;
Vertex[][] vertices;

boolean melting = false;


void initializeVertices()
{
    noiseSeed(millis());

    // create 2D array
    vertices = new Vertex[rowCount+1][columnCount+1];

    for (int i=0; i<=rowCount; i++)
    for (int j=0; j<=columnCount; j++)
    {
        // calculate position based on grid indices

        float x = j * gridSize - columnCount*gridSize/2;
        float y = 0;
        float z = i * gridSize - rowCount*gridSize/2;
        PVector position = new PVector(x, y, z);

        // calculate acceleration based on distance from
        // center of clock, using noise for correlation

        float noiseScale = .1 / gridSize;
        float accelerationScale = .01;

        float accelerationY = noise(i*noiseScale, j*noiseScale) 
          * max(dist(i, j, rowCount*.3, columnCount*.4), 2)
          * accelerationScale;

        PVector acceleration = new PVector(0, accelerationY, 0);

        // create new Vertex object

        vertices[i][j] = new Vertex(position, acceleration);
    }
}


void setup()
{
    size(1000, 1000, P3D);

    cam = new PeasyCam(this, 500);
    cam.rotateX(PI/4);
    cam.rotateY(PI/4);

    clock = loadImage("clock.png");
    initializeVertices();
}


void drawAxes()
{
    stroke(255, 0, 0);
    line(-100, 0, 0, 100, 0, 0);
    stroke(0, 255, 0);
    line(0, -100, 0, 0, 100, 0);
    stroke(0, 0, 255);
    line(0, 0, -100, 0, 0, 100);
}


void drawClock()
{
    noStroke();
    textureMode(NORMAL); 

    for (int i=0; i+1<=rowCount; i++)
    {
        beginShape(QUAD_STRIP);
        texture(clock);
        for (int j=0; j<=columnCount; j++)
        {
            vertex(vertices[i][j].position.x, vertices[i][j].position.y,
                vertices[i][j].position.z, ((float)j)/columnCount, ((float)i)/rowCount);

            vertex(vertices[i+1][j].position.x, vertices[i+1][j].position.y,
                vertices[i+1][j].position.z, ((float)j)/columnCount, (float)(i+1)/rowCount);
        }
        endShape();
    }
}


void updateVertices()
{
    if (melting)
    {
      for (Vertex[] row : vertices)
      for (Vertex v : row)
        v.update();
    }
}


void draw()
{
    background(0);
    drawAxes();

    drawClock();
    updateVertices();
}


void keyPressed()
{
    if (keyCode == ENTER)
      initializeVertices();
    else
      melting = true;
}


void keyReleased()
{
    melting = false;
}


class Vertex
{
    PVector position;
    PVector velocity;
    PVector acceleration;

    public Vertex(PVector position, PVector acceleration)
    {
        this.position = position.copy(); 
        this.velocity = new PVector();
        this.acceleration = acceleration.copy();
    }

    public void update()
    {
        position.add(velocity);
        velocity.add(acceleration);
    }
}


