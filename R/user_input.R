#!/usr/bin/env RScript

# from a rant on stack overflow
# readline() only works in interactive mode (not RScript)

user.input <- function(prompt) {
  if (interactive()) {
    return(readline(prompt))
  } else {
    cat(prompt)
    return(readLines("stdin", n=1))
  }
}

result = user.input("What is your name? ")
paste0("Hello, ", result, "!")

