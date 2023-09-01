
# install xcms

if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("xcms")


# in R interactive mode, run html server
# browseVignettes("xcms")

# BiocStyle required for xcms vignette examples to run (!)

if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("BiocStyle")

# and faahKO (wtf?!)

if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("faahKO")


# and pander and pheatmap (!)

install.packages("pander")
install.packages("pheatmap")


