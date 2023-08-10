#!/usr/bin/env nextflow

nextflow.enable.dsl = 2

params.outdir = "results" 
// default outdir, which can be specified on command line:
//   nextflow run process_fastqc.nf --outdir "my_results"

process FASTQC {

    tag {"FASTQC $sample_id"}
    label 'process_low'
    cpus 2

    publishDir "$params.outdir/fastqc_html", pattern: "*.html", mode: 'copy'
    publishDir "$params.outdir/fastqc_zip", pattern: "*.zip", mode: 'copy'

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
