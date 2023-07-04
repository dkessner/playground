#!/usr/bin/env groovy

// add a method to an existing class via its metaClass, using a closure,
// with 'delegate' referring to the original object

String.metaClass.double = { delegate.toLowerCase() * 2 }
println "Hello, World! ".double()

String.metaClass.multiple = { it -> delegate.toLowerCase() * 3 }
println "Hello, World! ".multiple(3)

// add pigLatin() to String

String.metaClass.pigLatin = {
    d = delegate.toLowerCase()
    d[1..-1] + d[0] + 'ay' 
}

println "Kessner".pigLatin()

// add fizzBuzz() to Integer

Integer.metaClass.fizzBuzz = {
    switch(delegate) {
        case {it%15==0}: return "FizzBuzz"
        case {it%3==0}: return "Fizz"
        case {it%5==0}: return "Buzz"
        default: return delegate
    }
}

println "1: ${1.fizzBuzz()}"
println "3: ${3.fizzBuzz()}"
println "5: ${5.fizzBuzz()}"
println "15: ${15.fizzBuzz()}"

def values = (1..30).collect {it.fizzBuzz()}
println(values)

// add a method with multiple input values

String.metaClass.concat = { text, n ->
    delegate + (" " + text)*n
}

println "World!".concat("Hello", 3)


