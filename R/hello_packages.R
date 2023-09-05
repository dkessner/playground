#!/usr/bin/env Rscript

# https://bookdown.org/ndphillips/YaRrr/packages.html
#install.packages("yarrr")

print("before library()")
library("yarrr")
print("after library()")

# all plots saved in Rplots.pdf

pirateplot(formula = weight ~ Time,
        data = ChickWeight,
        pal = "xmen")

# call without library()
yarrr::pirateplot(formula = weight ~ Diet,
                  data = ChickWeight)

print("Hello, world!")
print(".libPaths(): ")
print(.libPaths())


