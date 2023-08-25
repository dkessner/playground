#!/usr/bin/env nextflow


process doSomething {

    publishDir "results"

    input:
    val name 

    output:
    path output_file

    script:
    output_file = "${name}.out"

    """
    echo "Hello, world!" > $output_file
    """
}

workflow {
    names = channel.of("foo", "bar")
    names | doSomething | view
    // doSomething(names).view()
}


