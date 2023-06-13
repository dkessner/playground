#!/usr/bin/env nextflow


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
    ch = Channel.of("The", "quick", "brown", "fox")
    
    result = doSomething(ch) 
    result | collect | doSort | flatten | view
}

