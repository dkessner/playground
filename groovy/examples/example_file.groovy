#!/usr/bin/env groovy

def number = 0;
new File("quick_brown_fox.txt").eachLine { line ->
    number++;
    println "$number: $line"
}
