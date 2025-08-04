#!/usr/bin/env python
#
# bounce_module.py
#


import py5
from py5 import Py5Vector
from math import *


# https://py5coding.org/reference/py5vector.html


class Ball:

    def __init__(self):
        self.radius = py5.random(10, 30)
        self.position = Py5Vector(py5.width/2, py5.height/2)
        self.velocity = Py5Vector.from_heading(py5.random(0, 2*pi)) * py5.random(3, 5)
        self.color = py5.color(py5.random(255), py5.random(255), py5.random(255))

    def display(self):
        py5.fill(self.color)
        py5.ellipse(self.position.x, self.position.y, self.radius*2, self.radius*2)

        self.position += self.velocity

        if self.position.x < self.radius or \
           self.position.x > py5.width - self.radius:
            self.velocity.x *= -1

        if self.position.y < self.radius or \
           self.position.y > py5.height - self.radius:
            self.velocity.y *= -1


balls = []


def setup():
    py5.size(800, 800)
    #py5.full_screen()
    balls.append(Ball())

def draw():
    py5.background(0)
    for ball in balls:
        ball.display()

def key_pressed():
    balls.append(Ball())

py5.run_sketch()

