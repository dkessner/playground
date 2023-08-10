#!/usr/bin/env groovy

def x = 5 // local scope
println "x: $x " + x.getClass()

y = 6 // global scope
println "y: $y " + y.getClass()

def f()
{
    //println "x: $x " + x.getClass() // error!
    println "y: $y " + y.getClass()
}

f()
