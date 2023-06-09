#!/usr/bin/env nextflow 

// ./example_each -process.echo

params.outdir = "results"

process alignSequences {
  input:
  val seq
  each mode
  each lib

  """
  echo $seq $mode $lib
  """
}

workflow {
  sequences = Channel.from('juggling', 'computers', 'math')
  //methods = ['regular', 'espresso']
  methods = Channel.from('regular', 'espresso')
  libraries = [ 1, 2, 3]

  alignSequences(sequences, methods, libraries)
}
