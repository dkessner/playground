#!/usr/bin/env nextflow

//
// hello.nf
//

println "[hello.nf] hello from top"

process doSomething { 
    input: 
    val x 

    output: 
    stdout

    script: 
    """
    printf 'doSomething received: $x' 
    """
} 

process doSomething2 { 
    input: 
    val x 

    output: 
    stdout

    script: 
    """
    printf 'doSomething2 received: $x' 
    """
} 

//
// channel can be created outside of workflow
// TODO: what is the difference?
//
//greeting_ch = Channel.of('Hello', 'world!') 
//

// note: a process cannot be used twice in a workflow
// workaround: module aliasing: 
//  include { foo as bar } from './module'

workflow { 

    greeting_ch = Channel.of('Hello', 'world!') 
    results_ch = doSomething(greeting_ch) 
    results_ch.view { it } 

    // pipe syntax
    Channel.of('foo', 'bar') | doSomething2 | view

} 

println "[hello.nf] hello from bottom"

