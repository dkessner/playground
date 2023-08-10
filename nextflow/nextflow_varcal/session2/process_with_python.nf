#!/usr/bin/env nextflow

nextflow.enable.dsl=2

process PYTHON_SCRIPT {

  debug true // enable debug mode which prints the stdout

  script:
  """
  #!/usr/bin/env python
  import sys
  print("Hello from Python!")
  """

}

workflow {
  PYTHON_SCRIPT()
}

