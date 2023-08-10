#!/usr/bin/env nextflow

nextflow.enable.dsl=2

process BWA_INDEX {

  script:
  """
  pwd
  bwa index "../../../../repo/data/ref_genome/ecoli_rel606.fasta"  
  """
}

workflow {
  BWA_INDEX()
}

