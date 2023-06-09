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
    foo()
}


