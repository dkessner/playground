#!/usr/bin/env nextflow

// 
// example_include.nf
//

// note: the first 'include' runs all code in hello.nf, but the
// second 'include' does not

println "before include 1"
include { doSomething as foo } from './hello.nf'
println "after include 1"

println "before include 2"
include { doSomething2 as bar } from './hello.nf'
println "after include 2"

workflow {
    Channel.of('this', 'that', 'the other') | foo | view
    Channel.of('fee', 'fi', 'fo', 'fum') | bar | view
}

