#!/usr/bin/env groovy

// slashy strings

assert "abc" == /abc/
assert "\\d" == /\d/

def reference = "hello"
assert reference == /$reference/

// regular expressions

def twister = 'she sells sea shells at the sea shore of seychelles'

// twister must contain a substring of size 3
// that starts with s and ends with a
// regex find operator evaluates (casts?) to boolean
assert twister =~ /s.a/

def finder = (twister =~ /s.a/)
assert finder instanceof java.util.regex.Matcher

// twister must contain only words delimited by single spaces
// Regex match operator
assert twister ==~ /(\w+ \w+)*/

def WORD = /\w+/
matches = (twister ==~ /($WORD $WORD)*/)
assert matches instanceof java.lang.Boolean
assert !(twister ==~ /s.e/)

def wordsByX = twister.replaceAll(WORD, 'x')
assert wordsByX == 'x x x x x x x x x x'
def words = twister.split(/ /)
assert words.size() == 10
assert words[0] == 'she'
