#!/usr/bin/env nextflow

//
// example_output.nf
//

// https://www.nextflow.io/docs/latest/process.html#outputs

process randomNum {
  output:
  path 'random_num.txt'

  '''
  echo $RANDOM > random_num.txt
  '''
}


process foo {
  output:
  tuple path('foo1.txt'), path('foo2.txt', hidden: true)

  '''
  echo 'another new line' >> foo1.txt
  echo 'another new line' > foo2.txt
  '''
}


process splitLetters {
    output:
    path 'chunk_*'

    '''
    printf 'Hola' | split -b 1 - chunk_
    '''
}


workflow one {
    randomNum | view { "File: ${it.name} => ${it.text}" }
}


workflow two {
    foo | flatten | view { "File: ${it.name} => ${it.text}" }
}


workflow three {
    splitLetters
        | flatten
        | view { "File: ${it.name} => ${it.text}" }

}


workflow {
    one()
    two()
    three()
}

