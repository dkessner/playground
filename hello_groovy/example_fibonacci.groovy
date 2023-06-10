#!/usr/bin/env groovy

def time(Closure c, def arg)
{
    def start = System.nanoTime()
    result = c(arg) 
    def end = System.nanoTime()
    println "time: " + (end-start)
    return result
}

def fib
fib = {it<2 ? 1 : fib(it-1)+fib(it-2)}

assert time(fib, 40) == 165_580_141
assert time(fib, 40) == 165_580_141

// results caching
fib = fib.memoize()

assert time(fib, 40) == 165_580_141
assert time(fib, 40) == 165_580_141
assert time(fib, 40) == 165_580_141


