#!/usr/bin/env groovy

// https://www.timroes.de/groovy-tutorial-for-java-developers

println "hello, world!"

def x = 42
println x.getClass()
x = "Hello World"
println x.getClass()

// closures
// https://www.timroes.de/groovy-tutorial-for-java-developers-part2-closures

def hello = {
    println "[hello()] Hello!"
}

hello()

def do3 = {
    it()
    it()
    it()
}

do3 {println "hello there!"}


// collections
// https://www.timroes.de/groovy-tutorial-for-java-developers-part3-collections

def list = [1, 2, 3, 4]

println "list: " + list

println "3 in list: " + (3 in list)

list.each {println "value: " + it}

def even = list.findAll { it%2 == 0 }
println "even: " + even

def cubes = list.collect { it*it*it }
println "cubes: " + cubes

def squaresAndCubes = list.collectMany { [it*it, it*it*it] }
println "squaresAndCubes: " + squaresAndCubes

def upper = ["Hello", "World"].collect { it.toUpperCase() }
println "upper: " + upper

// spread-dot operator *. (call method on each element)
def upper2 = ["Hello", "World"]*.toUpperCase() 
println "upper2: " + upper2



