#!/usr/bin/env groovy

def benchmark(int repeat, Closure worker) {
    def start = System.nanoTime()
    repeat.times { worker(it) }
    def stop = System.nanoTime()
    return stop - start
}

def slow = benchmark(10000) { (int) it / 2 }
def fast = benchmark(10000) { it.intdiv(2) }

assert fast < slow

println "slow: $slow"
println "fast: $fast"
println()

// closure introspection

def paramCount(Closure c) {c.getParameterTypes()}

println paramCount { String s -> }
println paramCount { String s, int n -> }
println paramCount { String s, Integer n -> }
println paramCount { String s, def n -> }
println paramCount {}
println()

// closure in grep, switch, in

def odd = {it%2 == 1}

odds = [1, 2, 3, 4, 5].grep(odd)
println "[1, 2, 3, 4, 5].grep(odd): " + odds
assert odds == [1, 3, 5]

switch(5) {
    case odd : println "5 is odd"; assert true
}

if (2 in odd) assert false
assert (3 in odd)



