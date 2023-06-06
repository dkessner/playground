#!/usr/bin/env nextflow

nextflow.enable.dsl = 2

process FASTQC {

    input:
    tuple val(sample_id), path(reads)

    output:
    tuple val(sample_id), path("*.html"), path("*.zip")

    script:
    """
    fastqc ${reads}
    """
}

reads_ch = Channel.fromFilePairs("../repo/data/trimmed_fastq/SRR2584863_{1,2}.trim.fastq.gz", checkIfExists: true)

workflow {
  FASTQC(reads_ch)
  FASTQC.out.view()
}
