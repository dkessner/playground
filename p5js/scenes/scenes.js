let scene;

function setup() {
  createCanvas(400, 400);
  // Start with the first scene
  scene = new BouncingBallScene();
}

function draw() {
  background(220);
  scene.display();
}

function keyPressed() {
  if (key == '1') {
    scene = new BouncingBallScene();
  } else if (key == '2') {
    scene = new BouncingTriangleScene();
  } else {
    scene.keyPressed();
  }
}

class Scene {
  initialize() {}
  display() {}
  keyPressed() {}
}

class BouncingBallScene extends Scene {
  constructor() {
    super();
    this.balls = [];
  }

  initialize() {
    // Initialize any variables or state for the bouncing ball scene
  }

  display() {
    for (let ball of this.balls) {
      fill(ball.color);
      ellipse(ball.x, ball.y, ball.size, ball.size);
    }
  }

  keyPressed() {
    let newBall = {
      x: random(width),
      y: random(height),
      size: random(10, 50),
      color: color(random(255), random(255), random(255))
    };
    this.balls.push(newBall);
  }
}

class BouncingTriangleScene extends Scene {
  constructor() {
    super();
    this.color = color(0, 128, 255); // Initial color of the triangle
  }

  initialize() {
    // Initialize any variables or state for the bouncing triangle scene
  }

  display() {
    fill(this.color);
    noStroke();
    triangle(width/2, 100, width-50, height-50, 50, height-50);
  }

  keyPressed() {
    this.color = color(random(255), random(255), random(255)); // Change the triangle's color on key press
  }
}

