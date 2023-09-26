#!/usr/bin/env Rscript

# renv::init()
#   creates renv project structure
#
# - renv.lock
# - .Rprofile (source renv/activate.R)
# - renv
#   - activate.R
#   - settings.json
#   - .gitignore
#   - library

# renv::status()
#   gives status of packages (installed/recorded/used)

# renv::snapshot()
#   updates renv.lock

# renv::restore()
#   updates local environment

suppressMessages(library("yarrr"))
cat("Hello, world!\n")


