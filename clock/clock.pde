//
// clock.pde
//


import peasy.*;


PeasyCam cam;

PImage clock;

int rowCount = 10;
int columnCount = 10;
Vertex[][] vertices;


void setup()
{
    size(800, 600, P3D);

    cam = new PeasyCam(this, 100);
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

        vertices[i][j] = new Vertex(new PVector(x, y, z));
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


class Vertex
{
    PVector position;
    PVector velocity;
    PVector acceleration;

    public Vertex(PVector position)
    {
        this.position = position.copy(); 
        this.velocity = new PVector();
        this.acceleration = new PVector();
    }

    public void update()
    {
        position.add(velocity);
        velocity.add(acceleration);
    }
}



