#!/usr/bin/env nextflow

nextflow.enable.dsl=2

process BWA_INDEX {

    // optional directives
    tag {"BWA_INDEX $ref_genome"}
    label 'my_process'
    cpus 1

    publishDir "results/bwa_index", mode: "copy"
    
    input:
    path ref_genome

    output:
    path "${ref_genome}.bwt", emit: index

    script:
    """
    bwa index "$ref_genome"
    """
}

def ref_genome_path = "../repo/data/ref_genome/ecoli_rel606.fasta"

workflow {
    ref_genome_ch = Channel.fromPath(ref_genome_path)
    BWA_INDEX(ref_genome_ch)
    BWA_INDEX.out.view()
}

