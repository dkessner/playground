#!/usr/bin/env groovy

//
// p(n) == probability of no birthday collision in a group of n people
//

def p(int n)
{
    result = 1.0
    n.times {result *= (365-it)/365}
    return result
}

25.times {println it + " " + p(it).trunc(2)}

