#!/bin/bash
#
# pipeline.sh
#

set -e

data_dir=../repo/data
echo data_dir: $data_dir

results_dir=results_bash
mkdir $results_dir

genome=$data_dir/ref_genome/ecoli_rel606.fasta

bwa index $genome

pushd $results_dir
mkdir -p sam bam bcf vcf
popd

for fq1 in $data_dir/trimmed_fastq/*_1.trim.fastq.gz;
do
    echo "working with file $fq1"; base=$(basename $fq1 _1.trim.fastq.gz);  echo "base name is $base" \

    fq1=$data_dir/trimmed_fastq/${base}_1.trim.fastq.gz
    fq2=$data_dir/trimmed_fastq/${base}_2.trim.fastq.gz
    sam=$results_dir/sam/${base}.aligned.sam
    bam=$results_dir/bam/${base}.aligned.bam
    sorted_bam=$results_dir/bam/${base}.aligned.sorted.bam
    raw_bcf=$results_dir/bcf/${base}_raw.bcf
    variants=$results_dir/vcf/${base}_variants.vcf
    final_variants=$results_dir/vcf/${base}_final_variants.vcf

    bwa mem $genome $fq1 $fq2 > $sam
    samtools view -S -b $sam > $bam
    samtools sort -o $sorted_bam $bam
    samtools index $sorted_bam
    bcftools mpileup -O b -o $raw_bcf -f $genome $sorted_bam
    bcftools call --ploidy 1 -m -v -o $variants $raw_bcf
    vcfutils.pl varFilter $variants > $final_variants
done

