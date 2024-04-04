
function setup() {
  createCanvas(400, 400, WEBGL);
  
  // Enable debug mode.
  debugMode();
  
  describe('A multicolor box on a gray background. A grid and axes icon are displayed near the box.');
}

function draw() {
  background(200);
  
  // Enable orbiting with the mouse.
  orbitControl();
  
  // Style the box.
  normalMaterial();
  
  // Draw the box.
  box(20, 40);
}
