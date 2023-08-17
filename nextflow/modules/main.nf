#!/usr/bin/env nextflow

//
// main.nf
//

include { moduleName; moduleVersion; moduleProcess} from './module'

workflow {

    println "Hello, modules!"

    println "Running module: ${moduleName()} v${moduleVersion()}"

    channel.of("foo", "bar") | moduleProcess
}

