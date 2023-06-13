# Nextflow notes

## links

[Nextflow docs](https://nextflow.io/docs/latest/)

## notes

'''
nextflow.enable.dsl=2
'''

Echo stdout:
'''
nextflow run -process.echo
'''

## ideas

[csv handling](https://training.nextflow.io/basic_training/channels/#comma-separate-values-csv)

- use file objects for "value-like" queue channels (e.g. reference genome)
    https://bioinformatics.stackexchange.com/questions/20686/why-does-this-nextflow-script-finish-after-running-one-sample

- interesting handling of multiple channels
    https://stackoverflow.com/questions/75822947/combining-output-files-from-different-process-and-used-as-input-in-next-process
'''
    input:
    tuple(
        val(pair_id),
        val(tumor_sample), path(indexed_tumor_bam),
        val(normal_sample), path(indexed_normal_bam),
    )
    path indexed_fasta
'''


## further research

[Nextflow patterns](https://nextflow-io.github.io/patterns/)
[Data Carpentry: Data Wrangling Genomics](https://datacarpentry.org/wrangling-genomics/)
[Data Carpentry: Genomics Curriculum](https://datacarpentry.org/lessons/#genomics-workshop)


