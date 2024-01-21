//
// clock.pde
//


import peasy.*;

PeasyCam cam;

PImage clock;

int rowCount = 40;
int columnCount = 40;
Vertex[][] vertices;


void setup()
{
    size(800, 800, P3D);

    cam = new PeasyCam(this, 400);
    cam.rotateX(PI/4);
    cam.rotateY(PI/4);

    clock = loadImage("clock.png");
    vertices = new Vertex[rowCount+1][columnCount+1];

    int gridSize = 5;

    for (int i=0; i<=rowCount; i++)
    for (int j=0; j<=columnCount; j++)
    {
        float x = j * gridSize - columnCount*gridSize/2;
        float y = 0;
        float z = i * gridSize - rowCount*gridSize/2;
        PVector position = new PVector(x, y, z);

        PVector acceleration = new PVector();
        //if (i == 0 || i == rowCount || j == 0 || j == columnCount)

        float noiseScale = .05;
        float accelerationScale = .1;

        acceleration.y = noise(i*noiseScale, j*noiseScale) 
          * max(dist(i, j, rowCount*.3, columnCount*.4), 2)
          * accelerationScale;

        vertices[i][j] = new Vertex(position, acceleration);
    }
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

void draw()
{
    background(0);
    drawAxes();

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


void keyPressed()
{
    for (Vertex[] row : vertices)
    for (Vertex v : row)
      v.update();
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



