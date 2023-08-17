//
// module.nf
//

process hello_process {

    publishDir "${params.outdir}/${task.process}"

    input:
    val name

    output:
    path output_filename

    script:

    output_filename = "${name}.txt"

    """
    echo "Hello, world! ${task.index}" > $output_filename
    """
}
