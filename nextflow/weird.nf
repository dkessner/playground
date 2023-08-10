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

// this didn't work -- groovy source code not found (hidden by Nextflow?)
def getCode(Closure c) {
    c.metaClass.classNode.getDeclaredMethods("doCall")[0].code.text
}

workflow {
    
    println "weird.class: ${weird.class}\n"

    println "weird.class.declaredMethods: ${weird.class.declaredMethods.size()}"
    println weird.class.declaredMethods.name
    println ""

    println "weird.class.declaredFields: ${weird.class.declaredFields.size()}"
    println weird.class.declaredFields.name
    println ""

    println "weird.class.properties: ${weird.class.properties.size()}"
    println weird.class.properties.keySet()
    println ""

    println "weird.metaClass.properties: ${weird.metaClass.properties.size()}"
    println weird.metaClass.properties.name
    println ""

    println "weird.class.metaClass.methods: ${weird.metaClass.methods.size()}"
    println weird.metaClass.methods.name
    println ""

    filestems = channel.of("foo", "bar")
    filestems | weird

    println "weird.output: ${weird.output}"
    println "weird.taskBody: ${weird.taskBody}"
    println "weird.rawBody: ${weird.rawBody.toString()}"
    println "weird.getName(): ${weird.getName()}"
    println "weird.getDeclaredInputs(): ${weird.getDeclaredInputs()}"
    weird.getDeclaredInputs().each { println "input: ${it.toString()}" }
    println ""

}



