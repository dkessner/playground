#!/usr/bin/env nextflow

//
// hello_ls.nf
//

process dols { 
    input: 
    val x 

    output: 
    stdout

    script: 
    """
    echo "path: $x"
    ls $x | head
    """
} 

workflow { 
    Channel.of("..", "../..")
        | dols
        | view
} 

