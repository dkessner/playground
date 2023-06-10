#!/usr/bin/env groovy

class Drawing {
    List shapes
    def accept(Closure visitor) { shapes.each{it.accept(visitor)} }
}

class Shape {
    def accept(Closure visitor) { visitor(this) }
}

class Square extends Shape {
    def width
    def area() { width**2 }
}

class Circle extends Shape {
    def radius
    def area() { Math.PI * radius**2 }
}

def picture = new Drawing(shapes:
    [new Square(width:1), new Circle(radius:1)] )

def total = 0
picture.accept { total += it.area() }
println "The shapes in this drawing cover an area of $total units."

println 'The individual contributions are: '
picture.accept { println it.class.name + ":" + it.area() }

