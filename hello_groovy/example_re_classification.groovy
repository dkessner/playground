#!/usr/bin/env groovy

def fourLetters = ~/\w{4}/
println 'fourLetters pattern: ' + fourLetters

// Pattern class implements isCase(String) for classification,
// which allows use with: 'in', 'grep', and 'switch'

assert fourLetters.isCase('work')

// 'in' operator

println '\'love\' in fourLetters: ' + ('love' in fourLetters)
assert 'love' in fourLetters

// 'switch' statement

switch('beer'){
    case fourLetters: 
        println "case fourLetters"
        assert true
        break
    default: 
        assert false
}

// 'grep' method

beasts = ['bear','wolf','tiger','regex']
println beasts.grep(fourLetters)
assert beasts.grep(fourLetters) == ['bear','wolf']

