#!/usr/bin/env Rscript

#
# hello_rdata.R
#

# from YaRrr! 9.5
# https://bookdown.org/ndphillips/YaRrr/rdata-files.html

# create some objects

study1.df <- data.frame(id = 1:5, 
                        sex = c("m", "m", "f", "f", "m"), 
                        score = c(51, 20, 67, 52, 42))

score.by.sex <- aggregate(score ~ sex, 
                          FUN = mean, 
                          data = study1.df)

study1.htest <- t.test(score ~ sex, 
                       data = study1.df)


# ls(): list objects in workspace
cat("objects:", ls(), "\n")

filename_study = "study.RData"
filename_study_text = "study.txt"
filename_study_csv = "study.csv"
filename_everything = "everything.RData"

# save(): save specified objects
save(study1.df, study1.htest, file=filename_study)
cat("saving", filename_study, "\n")

# save.image(): save all objects in workspace
save.image(file=filename_everything)
cat("saving", filename_everything, "\n")

# rm(): remove objects
cat("removing objects\n")
rm(study1.df, score.by.sex, study1.htest)
cat("objects:", ls(), "\n\n")

# load(): load objects from file
load(file=filename_study)
cat("loading", filename_study, "\n")
cat("objects:", ls(), "\n\n")

load(file=filename_everything)
cat("loading", filename_everything, "\n")
cat("objects:", ls(), "\n\n")

# write.table(): write objects as text
cat("study1.df:\n")
print(study1.df)
cat("writing", filename_study_text, "\n")
write.table(x=study1.df, file=filename_study_text, sep=",", col.names=NA)

# write.csv(): convenience function 
#   for write.table(sep=",", col.names=NA)
# write.csv2(): European style
cat("writing", filename_study_csv, "\n")
write.csv(x=study1.df, file=filename_study_csv)


