#!/usr/bin/env nextflow


process weird {

    publishDir "results_weird"

    input:
        val filestem

    output:
        path output_file

    script:

    // causes error:
    //def output_file = "${filestem}.out"

    output_file = "${filestem}.out"

    """
    echo "Hello world" > $output_file
    """
}


workflow {
    
    println "weird.class: ${weird.class}"

    println "weird.class.declaredMethods: ${weird.class.declaredMethods.size()}"
    println weird.class.declaredMethods.name

    println "weird.class.declaredFields: ${weird.class.declaredFields.size()}"
    println weird.class.declaredFields.name

    println "weird.class.properties: ${weird.class.properties.size()}"
    println weird.class.properties

    println "weird.class.metaClass.properties: ${weird.metaClass.properties.size()}"
    println weird.class.metaClass.properties

    println "weird.class.output: ${weird.output}"
    println "weird.class.taskBody: ${weird.taskBody}"
    println "weird.class.getName(): ${weird.getName()}"

    filestems = channel.of("foo", "bar")
    filestems | weird
}



