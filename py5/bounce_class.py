#!/usr/bin/env python
#
# bounce_class.py
#


import py5
from py5 import Sketch, Py5Vector
from math import *


# https://py5coding.org/reference/py5vector.html


class Ball:

    def __init__(self, sIn):
        #self.s = py5.get_current_sketch() # does not appear to work (!)
        self.s = sIn
        self.radius = self.s.random(10, 30)
        self.position = Py5Vector(self.s.width/2, self.s.height/2)
        self.velocity = Py5Vector.from_heading(self.s.random(0, 2*pi)) * self.s.random(3, 5)
        self.color = self.s.color(self.s.random(255), self.s.random(255), self.s.random(255))

    def display(self):
        s = self.s
        position = self.position
        velocity = self.velocity
        radius = self.radius

        s.fill(self.color)
        s.ellipse(position.x, position.y, radius*2, radius*2)

        position += velocity

        if position.x < radius or \
           position.x > s.width - radius:
            velocity.x *= -1

        if position.y < radius or \
           position.y > s.height - radius:
            velocity.y *= -1



class Bounce(Sketch):

    def settings(self):
        #self.full_screen() # error abort (!)
        self.size(800, 800)

    def setup(self):
        self.balls = []

    def draw(self):
        self.background(0)
        for b in self.balls:
            b.display()

    def key_pressed(self):
        self.balls.append(Ball(self))


bounce = Bounce()
bounce.run_sketch()



