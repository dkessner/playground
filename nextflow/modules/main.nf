#!/usr/bin/env nextflow

//
// main.nf
//

include { hello_process } from './module'

workflow {
    channel.of("foo", "bar") | hello_process
}

