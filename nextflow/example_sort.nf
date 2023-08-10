#!/usr/bin/env nextflow

nextflow.enable.dsl=2

process doSomething {

    input:
    val x

    output:
    val x

    script:
    x = "word_"+x

    """
    echo "Hello $x"
    """
}


process doSort {
    
    input:
    val list

    output:
    val list

    script:
    list = list.sort()
    """
    echo "sorting"
    """
}


workflow {
    ch = Channel.of("the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog")
    
    result = doSomething(ch) 
    result | collect | doSort | flatten | view
}

