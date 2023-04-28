
println "hello from the top of example_template.nf"

process templateExample {
    input:
    val STR

    output:
    stdout

    script:
    template 'my_script.sh'
}

process templateExample2 {
    input:
    val STR

    output:
    stdout

    script:
    template 'my_script.sh'
}


workflow {
    Channel.of('this', 'that') | templateExample | view
}


println "hello from the bottom of example_template.nf"

