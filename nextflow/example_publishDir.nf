#!/usr/bin/env nextflow

process foo {
    publishDir 'results'

    output:
    path 'chunk_*'

    '''
    printf 'Hola' | split -b 1 - chunk_
    '''
}

workflow {
    ch = foo()

    // print channel 
    ch.view()

    // print number of items emitted from channel (1)
    ch.count().view()
}


