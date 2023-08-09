#!/usr/bin/env groovy

def text = "The quick brown fox jumps over the lazy dog."

println "class: ${text.class}"
println "text.class.declaredMethods: ${text.class.declaredMethods.size()}"
println "text.class.declaredFields: ${text.class.declaredFields.size()}"
println "field names: ${text.class.declaredFields.name}"

println "text.class.properties: ${text.class.properties}"


