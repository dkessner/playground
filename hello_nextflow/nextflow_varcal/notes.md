# Nextflow tutorial - variant calling pipeline

[tutorial](https://sateeshperi.github.io/nextflow_varcal/nextflow/)
[repo](https://github.com/sateeshperi/nextflow_varcal)
[Sateesh Peri](https://github.com/sateeshperi)

dependencies:
    bwa
    samtools
    bcftools
    fastqc

## useful

[csv handling](https://training.nextflow.io/basic_training/channels/#comma-separate-values-csv)

## further research

[Nextflow patterns](https://nextflow-io.github.io/patterns/)
[Data Carpentry: Data Wrangling Genomics](https://datacarpentry.org/wrangling-genomics/)
[Data Carpentry: Genomics Curriculum](https://datacarpentry.org/lessons/#genomics-workshop)

## notes

Echo stdout:
'''
nextflow run -process.echo
'''

## ideas

- use file objects for "value-like" queue channels (e.g. reference genome)
    https://bioinformatics.stackexchange.com/questions/20686/why-does-this-nextflow-script-finish-after-running-one-sample


