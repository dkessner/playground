#!/usr/bin/env nextflow

// reference:
//   https://training.nextflow.io/basic_training/intro/#nextflow-code

process SPLITLETTERS { 
    input: 
    val x 

    output: 
    path 'chunk_*' 

    script: 
    """
    printf '$x' | split -b 6 - chunk_
    """
} 

process CONVERTTOUPPER { 
    input: 
    path y 

    output: 
    stdout 

    script: 
    """
    cat $y | tr '[a-z]' '[A-Z]'
    """
} 

workflow workflow_function { 

    // function notation

    greeting_ch = Channel.of('Hello world!') 
    letters_ch = SPLITLETTERS(greeting_ch) 
    results_ch = CONVERTTOUPPER(letters_ch.flatten()) 
    results_ch.view()
}

workflow workflow_pipe {

    // pipe notation

    Channel.of('!Hola mundo!') 
        | SPLITLETTERS 
        | flatten
        | CONVERTTOUPPER 
        | view

    // or assign result channel with:
    //  | set { mych }
    // then:
    // mych.view()
}

workflow workflow_mixed {

    // pipe notation for processes,
    // function notation for operators

    ch = Channel.of('Ca va monde!') | SPLITLETTERS 
    ch2 = ch.flatten() | CONVERTTOUPPER 
    ch2.view()
} 

workflow {
    workflow_function()
    workflow_pipe()
    workflow_mixed()
}


