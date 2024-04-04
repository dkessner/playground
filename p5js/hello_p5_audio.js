//
// hello_p5_audio.js
//


// must run local web server


let mic;


function setup() {
  createCanvas(710, 200);

  // some browsers (e.g. Chrome) require user interaction before 
  // allowing initialization of an audio context
  getAudioContext().suspend();
}


function initializeMicrophone() {
  userStartAudio(); // starts audio context
  mic = new p5.AudioIn();
  mic.start();
}


function draw() {
  background(200);

  text("audio context state: " + getAudioContext().state, 50, 50);

  let vol = 0;

  if (mic) {
      vol = mic.getLevel(); // in [0,1]
  }

  let h = map(vol, 0, 1, height, 0);
  fill(127);
  stroke(0);
  ellipse(width/2, h-25, 50, 50);
}


function mousePressed() {
    initializeMicrophone();
}


