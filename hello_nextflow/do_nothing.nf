process do_nothing {
    publishDir "$params.outdir/bams"

    input:
    tuple val(meta), path(bam), path(bai)

    output:
    path bam

    script:
    '''
    echo "do_nothing"
    '''
}

//    do_nothing(bam_bai) // dk

