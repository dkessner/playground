//
// clock.pde
//


PImage clock;

int rowCount = 10;
int columnCount = 10;
Vertex[][] vertices;


void setup()
{
    size(800, 600, P3D);
    clock = loadImage("clock.png");


    vertices = new Vertex[rowCount+1][columnCount+1];

    int gridSize = 10;

    for (int i=0; i<=rowCount; i++)
    for (int j=0; j<=columnCount; j++)
    {
        PVector position = new PVector(j*gridSize, i*gridSize, 0);
        vertices[i][j] = new Vertex(position);
    }
}


void draw()
{
    background(0);

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



