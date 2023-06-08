#!/usr/bin/env groovy

def p(int n)
{
    result = 1
    n.times {result *= (365-it)/365}
    return result
}

println p(3)
25.times {println it + " " + p(it)}


