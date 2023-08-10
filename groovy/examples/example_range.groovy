#!/usr/bin/env groovy

assert (0..10).contains(0)
assert (0..10).contains(5)
assert (0..10).contains(10)
assert (0..10).contains(-1) == false
assert (0..10).contains(11) == false
assert (0..<10).contains(9)
assert (0..<10).contains(10) == false

def a = 0..10
assert a instanceof Range
assert a.contains(5)

a = new IntRange(0,10)
assert a.contains(5)

assert (0.0..1.0).contains(1.0)
assert (0.0..1.0).containsWithinBounds(0.5)


def today     = new Date()
def yesterday = today - 1
assert (yesterday..today).size() == 2
assert ('a'..'c').contains('b')

def log = ''
for (element in 5..9) {
    log += element
}
assert log == '56789'

log = ''
for (element in 9..5){
    log += element
}
assert log == '98765'
log = ''
(9..<5).each { element ->
    log += element
}
assert log == '9876'

def age = 36
switch(age){
    case 16..20 : insuranceRate = 0.05 ; break
    case 21..50 : insuranceRate = 0.06 ; break
    case 51..65 : insuranceRate = 0.07 ; break

    default: throw new IllegalArgumentException()
}
assert insuranceRate == 0.06

def ages = [20, 36, 42, 56]
def midage = 21..50
assert ages.grep(midage) == [36, 42]


