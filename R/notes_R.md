# Notes - R

[R for Data Science (2e) - Hadley Wickham](https://r4ds.hadley.nz/)  

```
install.packages("tidyverse")
```

[Hands-On Programming with R](https://rstudio-education.github.io/hopr/)

[Tidy Modeling with R](https://www.tmwr.org/)  


## Rocker / Docker

[Rocker Project](https://rocker-project.org/)  


Run R in container:
```
docker run --rm -ti r-base
```

Run RStudio ([localhost:8787](http://localhost:8787), rstudio/yourpassword):

```
docker run --rm -ti -e PASSWORD=yourpassword -p 8787:8787 rocker/rstudio
```


## Recommendations

For large data (10-100GB): use package
[data.table](https://github.com/Rdatatable/data.table)

