//
// module.nf
//


def double_string(s) {s+s}


process hello_process {

    publishDir "${params.outdir}/hello_process"

    input:
    val name

    output:
    path output_filename

    script:

    output_filename = "${name}.txt"

    """
    echo "Hello, world! ${task.index}" > $output_filename
    echo "${double_string(name + " ")}" >> $output_filename
    """
}

