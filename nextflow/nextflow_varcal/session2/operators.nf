#!/usr/bin/env nextflow

//
// operators.nf
//


chr_ch = channel.of(1..22, 'X', 'Y')

autosomes_ch = chr_ch.filter(Number)
autosomes_ch.filter {it < 5}
            .view {"chr" + it}

// regular expression filtering
autosomes_ch.filter(~/^2.*/)
            .view {"chr$it"}


channel.fromPath("../repo/data/untrimmed_fastq/*.fastq.gz")
       .map ({ file -> [file, file.countFastq()] })
       .filter({ file, numreads -> numreads > 25000})
       .view ({ file, numreads -> "file $file contains $numreads reads" })

// flatten(): list -> multiple items (like Channel.fromList)
list1 = ['a','b','c']
channel.of(list1)
       .flatten()
       .view()

// collect(): multiple items -> single list
channel.of(1, 2, 3, 4)
        .collect()
        .view()


// groupTuple(): group by shared key
channel.of( ['tuple:wt','wt_1.fq'], ['tuple:wt','wt_2.fq'], ['tuple:mut','mut_1.fq'], ['tuple:mut', 'mut_2.fq'] )
            .groupTuple()
            .view()

// mix(): merge channels
ch1 = channel.of( 'mix:1', 'mix:2', 'mix:3' )
ch2 = channel.of( 'mix:X', 'mix:Y' )
ch3 = channel.of( 'mix:mt' )
ch1.mix(ch2, ch3).view()


// join(): combine channels by matching key
reads1_ch = channel.of(['join:wt', 'wt_1.fq'], ['join:mut','mut_1.fq'])
reads2_ch = channel.of(['join:wt', 'wt_2.fq'], ['join:mut','mut_2.fq'])
reads1_ch.join(reads2_ch)
         .view()


// into(): deprecated fork
/*
channel.of('chr1', 'chr2', 'chr3')
       .into({ch1; ch2})
ch1.view {"ch1: $it"}
ch2.view {"ch2: $it"}
*/

// tap(): fork

Channel
    .of ( 'tap:a', 'tap:b', 'tap:c' )
    .tap { log1 } // note: tap(log1) gives error
    .map { it * 2 }
    .tap { log2 }
    .map { it.toUpperCase() }
    .view { "tap Result: $it" }

log1.view { "tap log1: $it" }
log2.view { "tap log2: $it" }

// count(): returns total # of items in channel
ch = channel.of(1..22,'X','Y')
            .count()
            .view {"count: $it"}


// splitCSV()

channel.fromPath("samples.csv")
       .splitCsv()
       .view() {println "splitCSV:\n\t" + it[0] + "\n\t" + it[1] + "\n\t" + it[2]}

channel.fromPath("samples.csv")
       .splitCsv(header:true)
       .view({"splitCSV(header):" + it.fastq_1}) // access by column name


