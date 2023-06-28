#!/usr/bin/env groovy

@Grab(group='com.opencsv', module='opencsv', version='5.7.1')

import com.opencsv.*

CSVReader reader = new CSVReaderBuilder(new FileReader("test.csv")).build();
List<String[]> myEntries = reader.readAll();

println("hello")

println myEntries[0]
println myEntries[1]

