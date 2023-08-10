#!/usr/bin/env nextflow

//
// example_template.nf
//

process templateExample {
    input:
    val STR

    output:
    stdout

    script:
    template 'my_script.sh' // note: nextflow searches 'templates' folder
}

workflow {
    Channel.of('this', 'that') | templateExample | view
}

