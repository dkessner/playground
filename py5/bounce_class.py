#!/usr/bin/env python
#
# bounce_class.py
#


from py5 import Sketch, Py5Vector
from math import *


# https://py5coding.org/reference/py5vector.html


class Ball:

    def __init__(self, sketch):
        self.sketch = sketch
        self.radius = sketch.random(10, 30)
        self.position = Py5Vector(sketch.width/2, sketch.height/2)
        self.velocity = Py5Vector.from_heading(sketch.random(0, 2*pi)) * self.sketch.random(3, 5)
        self.color = sketch.color(sketch.random(255), sketch.random(255), sketch.random(255))

    def display(self):
        self.sketch.fill(self.color)
        self.sketch.ellipse(self.position.x, self.position.y, self.radius*2, self.radius*2)

        self.position += self.velocity

        if self.position.x < self.radius or \
           self.position.x > self.sketch.width - self.radius:
            self.velocity.x *= -1

        if self.position.y < self.radius or \
           self.position.y > self.sketch.height - self.radius:
            self.velocity.y *= -1



class Bounce(Sketch):

    def settings(self):
        #self.full_screen()
        self.size(800, 800)

    def setup(self):
        self.ball = Ball(self)

    def draw(self):
        self.background(0)
        self.ball.display()


bounce = Bounce()
bounce.run_sketch()

