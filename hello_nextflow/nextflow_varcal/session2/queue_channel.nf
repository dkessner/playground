#!/usr/bin/env nextflow

ch1 = Channel.of(1, 2, 3, 4, 5)

ch2 = Channel.fromList([6, 'seven', 8])

ch3 = Channel.fromPath("../*")

ch1.view()
ch2.view()
ch3.view()

