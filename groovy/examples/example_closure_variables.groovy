#!/usr/bin/env groovy

// https://groovy-lang.org/closures.html

// The binding object stores all variables that were defined without
// specifying their types or using def keyword:
// https://stackoverflow.com/questions/52839085/finding-list-map-of-free-variables-of-a-closure-in-groovy

//
// Closure variable scope:
//
// 1) variable declared (def/type) within scope of closure: local to closure
//    scope
//
// 2) variable defined in enclosing scope: closure keeps reference
//
// 3) variable defined (set) within closure, but not declared: added/updated
//    in binding object (at runtime, when closure is called).  Note:  binding
//    object is owned by script (singleton?)
//


def value = 420

Closure addToValue = { println "addToValue($it)"; value += it; a = 7}

println "addToValue: ${addToValue.class.name}"
println "paramTypes: ${addToValue.getParameterTypes()}"
println ""

println "value: $value"
println "binding variables: ${addToValue.getBinding().getVariables()}"
println ""

addToValue(3)
println "value: $value"
println "binding variables: ${addToValue.getBinding().getVariables()}"
println ""

Closure addToValueTwice = { println "addToValueTwice($it)"; value += 2*it; a *= 2; b = 666}
println "addToValueTwice: ${addToValueTwice.class.name}"
println "paramTypes: ${addToValueTwice.getParameterTypes()}"
println ""

addToValueTwice(5)
println "value: $value"
println "binding variables: ${addToValue.getBinding().getVariables()}"
println ""

println "global binding variables: ${getBinding().getVariables()}"



