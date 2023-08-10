#!/usr/bin/env nextflow 

nextflow.enable.dsl = 2

process TUPLEINPUT {

  // debug true 
  // or: nextflow run -process.echo

  input:
  tuple val(sample_id), path(reads)

  script:
  """
  echo ${sample_id}
  echo ${reads}
  """
}

reads_ch = Channel.fromFilePairs("../repo/data/trimmed_fastq/SRR2584863_{1,2}.trim.fastq.gz")

workflow {
  TUPLEINPUT(reads_ch)
}
