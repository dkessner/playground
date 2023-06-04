#!/usr/bin/env groovy

def benchmark(int repeat, Closure worker) {
    def start = System.nanoTime()
    repeat.times { worker(it) }
    def stop = System.nanoTime()
    return stop - start
}

def slow = benchmark(10000) { (int) it / 2 }
def fast = benchmark(10000) { it.intdiv(2) }

println "slow: $slow"
println "fast: $fast"

assert fast * 2 < slow

