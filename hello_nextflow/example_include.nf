
println "before include 1"
include { templateExample as foo } from './example_template.nf'
println "after include 1"

println "before include 2"
include { templateExample2 as bar } from './example_template.nf'
println "after include 2"

workflow {
    Channel.of('this', 'that', 'the other') | foo | view
    Channel.of('fee', 'fi', 'fo', 'fum') | bar | view
}

