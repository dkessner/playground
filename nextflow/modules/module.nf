//
// module.nf
//



def moduleName() {
    "MyModule"
}

def moduleVersion() {
    "1.0"
}

process moduleProcess {

    publishDir "${params.outdir}/hello_process"

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

