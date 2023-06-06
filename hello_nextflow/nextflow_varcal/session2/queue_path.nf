#!/usr/bin/env nextflow

println("Single File")
read_ch = Channel.fromPath("../repo/data/untrimmed_fastq/SRR2584863_1.fastq.gz")
read_ch.view()

println("Glob Syntax")

// We can change the default options for the `fromPath` method to give an error if the file doesn’t exist using the `checkIfExists` parameter.
read_ch = Channel.fromPath( "../repo/data/**/*.fastq.gz", checkIfExists: true )
read_ch.view()
