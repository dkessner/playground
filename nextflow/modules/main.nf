#!/usr/bin/env nextflow

//
// main.nf
//

include {hello_process as p; double_string as f} from './module'

workflow {

    println f("Hello, modules! ")

    channel.of("foo", "bar") | p
}

