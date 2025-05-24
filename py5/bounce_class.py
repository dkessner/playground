#!/usr/bin/env python
#
# bounce_class.py
#


import py5
from py5 import Sketch, Py5Vector
from math import *


# https://py5coding.org/reference/py5vector.html


class Ball:

    def __init__(self):
        self.s = py5.get_current_sketch()
        self.radius = self.s.random(10, 30)
        self.position = Py5Vector(self.s.width/2, self.s.height/2)
        self.velocity = Py5Vector.from_heading(self.s.random(0, 2*pi)) * self.s.random(3, 5)
        self.color = self.s.color(self.s.random(255), self.s.random(255), self.s.random(255))

    def display(self):
        self.s.fill(self.color)
        self.s.ellipse(self.position.x, self.position.y, self.radius*2, self.radius*2)

        self.position += self.velocity

        if self.position.x < self.radius or \
           self.position.x > self.s.width - self.radius:
            self.velocity.x *= -1

        if self.position.y < self.radius or \
           self.position.y > self.s.height - self.radius:
            self.velocity.y *= -1



#class Bounce(Sketch):
#
#    def settings(self):
#        #self.full_screen()
#        self.size(800, 800)
#
#    def setup(self):
#        self.ball = Ball(self)
#
#    def draw(self):
#        self.background(0)
#        self.ball.display()


#bounce = Bounce()
#bounce.run_sketch()
#


balls = []

def settings():
    py5.full_screen()
    #py5.size(800, 800)

def setup():
    balls.append(Ball())

def draw():
    py5.background(0)
    for b in balls:
        b.display()

def key_pressed():
    balls.append(Ball())

py5.run_sketch()

