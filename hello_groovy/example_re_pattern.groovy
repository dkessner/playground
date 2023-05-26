#!/usr/bin/env groovy

def twister = 'she sells sea shells at the sea shore of seychelles'

// some more complicated regex:
// word that starts and ends with same letter

def regex = /\b(\w)\w*\1\b/
def many  = 100 * 1000


start = System.nanoTime()
many.times{
    twister =~ regex
}
timeImplicit = System.nanoTime() - start

start = System.nanoTime()
pattern = ~regex
many.times{
    pattern.matcher(twister)
}
timePredef = System.nanoTime() - start

println "timeImplicit: $timeImplicit"
println "timePredef: $timePredef"

assert timeImplicit > timePredef 
